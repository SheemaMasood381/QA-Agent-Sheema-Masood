import sys
import os
import json
import streamlit as st
from dotenv import load_dotenv
from datetime import datetime
import shutil

# Local packages ka path
sys.path.append(os.path.abspath("src"))

from ingest.youtube_transcript import get_youtube_transcript, chunk_transcript
from qa_gen.generate_test_cases import generate_test_cases
from qa_gen.markdown_to_json import from_markdown  # ✅ added for markdown ➜ JSON
from playwright_gen.script_generator import json_to_playwright_tests
from runner.test_runner import run_playwright_tests, parse_test_results

# ENV & paths
load_dotenv()
GROQ_API_KEY   = os.getenv("GROQ_API_KEY")

TRANSCRIPT_TXT = "data/transcripts/recruter_transcript.txt"
TEST_CASES_JSON = "data/test_cases/test_cases.json"
TEST_CASES_MD = "data/test_cases/test_cases_combined.md"
SCRIPT_PATH    = "tests/generated.spec.ts"
RESULTS_DIR    = "results"
HISTORY_DIR    = "data/test_cases/history"

st.set_page_config("QAgenie – Recruter.ai", layout="centered")
st.title("🤖 QAgenie – Recruter.ai One Click Automation")

yt_url = st.text_input("🎮 Paste Recruter.ai YouTube URL")

if st.button("🚀 Run All Steps (One Click)"):
    # Step 1: Transcript
    try:
        os.makedirs(os.path.dirname(TRANSCRIPT_TXT), exist_ok=True)
        path = get_youtube_transcript(yt_url, TRANSCRIPT_TXT)
        st.success(f"✅ [1/5] Transcript saved ➔ `{path}`")
    except Exception as e:
        st.error(f"Transcript error: {str(e)}")
        st.stop()

    # Step 2: Generate Test Cases via Groq
    if not GROQ_API_KEY:
        st.error("Set GROQ_API_KEY in your .env")
        st.stop()
    try:
        chunks = chunk_transcript(TRANSCRIPT_TXT)
        cases, md_chunks = generate_test_cases(chunks, GROQ_API_KEY)
        st.success(f"✅ [2/5] {len(cases)} raw test cases generated.")
        os.makedirs("data/test_cases", exist_ok=True)

        # --- Markdown to structured JSON ---
        structured_cases = from_markdown("\n".join(md_chunks))

        # Save JSON
        with open(TEST_CASES_JSON, "w", encoding="utf-8") as f_json:
            json.dump(structured_cases, f_json, indent=2)

        # Save Markdown
        with open(TEST_CASES_MD, "w", encoding="utf-8") as f_md:
            for md in md_chunks:
                f_md.write(md + "\n")

    except Exception as e:
        st.error(f"Test case generation error: {str(e)}")
        st.stop()

    # Step 3: Convert to Playwright
    try:
        json_to_playwright_tests(TEST_CASES_JSON, SCRIPT_PATH)
        st.success("✅ [3/5] Playwright script generated.")
    except Exception as e:
        st.error(f"Playwright conversion error: {str(e)}")
        st.stop()

    # ---------- Step 4: Run Playwright Tests ----------
try:
    os.makedirs(RESULTS_DIR, exist_ok=True)
    result = run_playwright_tests(SCRIPT_PATH)   # ← rc → result

    if result.returncode == 0:
        st.success("✅ [4/5] Playwright tests executed.")
    else:
        st.error("❌ Playwright exited with errors:")
        st.code(result.stderr or "(no stderr)")
        st.stop()

except Exception as e:
    st.error(f"Playwright test run error: {str(e)}")
    st.stop()


    # Step 5: Parse Results
st.subheader("📊 [5/5] Result Summary")
try:
    results = parse_test_results(RESULTS_DIR)
    if not isinstance(results, dict):
        st.error("⚠️ Unexpected result format from test parser.")
        st.json(results)
    elif results.get("failed", 0) > 0:
        st.json(results)
        st.error(f"❌ {results.get('failed', 0)} test(s) failed.")
    elif results.get("total", 0) == 0:
        st.json(results)
        st.warning("⚠️ No tests executed or no results found.")
    else:
        st.json(results)
        st.success("🎉 All tests passed!")
except FileNotFoundError:
    st.error("❌ Test result file not found. Did Playwright run and generate a JSON report?")
except Exception as e:
    st.error(f"Result parsing error: {e}")

    # Archive
    now_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    hist_folder = os.path.join(HISTORY_DIR, now_str)
    try:
        os.makedirs(hist_folder, exist_ok=True)
        shutil.copy(TEST_CASES_JSON, os.path.join(hist_folder, "test_cases.json"))
        shutil.copy(TEST_CASES_MD, os.path.join(hist_folder, "test_cases.md"))
        st.info(f"🗂️ Archived to `{hist_folder}`")
    except Exception as e:
        st.warning(f"History archiving failed: {str(e)}")

    # --- Download buttons ---
    st.download_button(
        label="⬇️ Download test_cases.json",
        data=json.dumps(structured_cases, indent=2),
        file_name="test_cases.json",
        mime="application/json"
    )
    with open(TEST_CASES_MD, "r", encoding="utf-8") as f_md:
        md_content = f_md.read()
        st.download_button(
            label="⬇️ Download test_cases.md",
            data=md_content,
            file_name="test_cases.md",
            mime="text/markdown"
        )

    # Markdown preview
    st.markdown("### 📋 Test Cases (Markdown Preview)")
    st.markdown(md_content)

# ---- HISTORY SECTION IN SIDEBAR ----
with st.sidebar:
    st.markdown("#### 📜 Previous Test‑Case Generations (History)")
    if os.path.exists(HISTORY_DIR):
        history_dirs = sorted(os.listdir(HISTORY_DIR), reverse=True)
        for h in history_dirs:
            hist_json = f"{HISTORY_DIR}/{h}/test_cases.json"
            hist_md = f"{HISTORY_DIR}/{h}/test_cases.md"
            cols = st.columns(2)
            if os.path.exists(hist_json):
                with open(hist_json, "r", encoding="utf-8") as f_hist:
                    cols[0].download_button(
                        f"📄 {h} (json)",
                        data=f_hist.read(),
                        file_name=f"test_cases_{h}.json",
                        mime="application/json",
                        key=f"{h}-json"
                    )
            if os.path.exists(hist_md):
                with open(hist_md, "r", encoding="utf-8") as f_hist_md:
                    cols[1].download_button(
                        f"📄 {h} (md)",
                        data=f_hist_md.read(),
                        file_name=f"test_cases_{h}.md",
                        mime="text/markdown",
                        key=f"{h}-md"
                    )
    else:
        st.info("No history yet – generate test cases first.")



# Footer
import streamlit as st

st.markdown(
    """
    <hr style="margin-top: 2em; margin-bottom: 0.5em; border-top: 1px solid #bbb;">
    <div style="text-align: center; color: #6c757d;">
        <span style="font-size:1.1em;">🤖 <b>QAgenie</b> by <b>Sheema Masood</b></span>
        <br>
        <a href="https://www.linkedin.com/in/sheema-masood/" target="_blank" style="text-decoration:none; color:#0a66c2; margin-right:7px;">
            <b>LinkedIn</b>
        </a> 
        |
        <a href="https://github.com/sheemamasood381/" target="_blank" style="text-decoration:none; color:#333; margin-left:7px;">
            <b>GitHub</b>
        </a>
        <br>
        <span style="font-size:0.98em;">
            <i>Supercharged by</i> <b>Groq</b> · <b>OpenAI</b> · <b>Langchain</b> – <i>Open Source Spirit</i>
        </span><br>
        <span style="font-size:0.95em; color:#999;">Automating Recruter.ai, one test at a time.</span>
    </div>
    """,
    unsafe_allow_html=True
)