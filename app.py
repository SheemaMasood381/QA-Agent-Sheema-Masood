import streamlit as st
import os
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
from groq import Groq
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, VideoUnavailable

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Prepare output folders
os.makedirs("data/transcripts", exist_ok=True)
os.makedirs("data/test_cases", exist_ok=True)

def get_youtube_transcript(video_url: str, save_path: str):
    try:
        # Clean video ID only
        video_id = video_url.split("v=")[-1].split("&")[0]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        with open(save_path, "w", encoding="utf-8") as f:
            for entry in transcript:
                f.write(f"{entry['text']}\n")
        return save_path
    except NoTranscriptFound:
        print("🚫 No transcript found for this video (maybe no captions available).")
    except VideoUnavailable:
        print("🚫 Video is unavailable (private, deleted, or region blocked).")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

def chunk_transcript(transcript_path: str, chunk_size: int = 600):
    with open(transcript_path, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i+chunk_size])
        if chunk.strip():
            chunks.append(chunk)
    return chunks

def generate_test_cases_groq(chunks, groq_api_key, model="llama3-70b-8192"):
    client = Groq(api_key=groq_api_key)
    all_cases = []
    for idx, chunk in enumerate(chunks):
        prompt = (
            "You are QAgenie, an AI QA assistant for frontend testing.\n"
            "Given the following instructions, generate Playwright test cases covering:\n"
            "- Core user flows\n- Edge cases (invalid data, boundaries, network)\n"
            "- Cross-browser & mobile\n- Accessibility\n- Performance\n"
            "Output each test case as:\n"
            "Title: ...\nSteps: ...\nExpected Result: ...\nEdge Cases: ...\nAccessibility: ...\n\n"
            f"Instructions:\n{chunk}\n"
        )
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are QAgenie, a thorough QA assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1200
        )
        content = response.choices[0].message.content
        all_cases.append(content)
        with open(f"data/test_cases/test_cases_{idx+1}.md", "w", encoding="utf-8") as f:
            f.write(content)
    return all_cases

# ------------------- STREAMLIT UI -------------------
st.set_page_config(page_title="QAgenie – Recruter.ai QA Agent", layout="centered")
st.title("🤖 QAgenie – Recruter.ai Automated QA Agent")

st.markdown("""
Paste the **Recruter.ai "How to" YouTube video URL** below and click **Generate & Test**.
This agent will:
- Extract the video transcript
- Generate Playwright-ready frontend test cases using Groq Llama3
- Display the test cases for you (Markdown and download)
""")

video_url = st.text_input("YouTube video URL", placeholder="https://www.youtube.com/watch?v=xyz123abc")
run_button = st.button("Generate & Test")

transcript_path = "data/transcripts/recruterai_howto.txt"

if run_button and video_url:
    with st.spinner("Extracting transcript..."):
        get_youtube_transcript(video_url, transcript_path)
    st.success("Transcript extracted!")

    with st.spinner("Chunking transcript..."):
        chunks = chunk_transcript(transcript_path)
    st.success(f"Transcript split into {len(chunks)} chunks.")

    with st.spinner("Generating test cases via Groq (Llama3)..."):
        test_cases = generate_test_cases_groq(chunks, GROQ_API_KEY)
    st.success("Test cases generated!")

    st.subheader("Generated Test Cases (Markdown)")
    for idx, case_md in enumerate(test_cases, 1):
        st.markdown(f"### Test Case Chunk {idx}")
        st.markdown(case_md)
        st.download_button(
            label=f"Download Test Case Chunk {idx}",
            data=case_md,
            file_name=f"test_case_chunk_{idx}.md",
            mime="text/markdown",
            key=f"dl_{idx}"
        )
    st.info("Next step: (Optional) Run Playwright tests and show results!")

elif run_button:
    st.error("Please paste a valid YouTube video URL.")

st.markdown("---")
st.caption("Built by Sheema Masood • Powered by Open Source & Groq Llama3 🚀")