from groq import Groq
import json, re, os

def generate_test_cases(chunks, api_key, model="llama3-70b-8192"):
    client = Groq(api_key=api_key)
    all_cases, md_chunks = [], []

    os.makedirs("data/test_cases/debug_raw", exist_ok=True)

    for idx, chunk in enumerate(chunks, 1):
        prompt = (
            "You are QAgenie, an AI QA assistant for frontend testing.\n"
            "Generate Playwright test cases as a JSON array (title, steps, expected_result ...).\n"
            f"INSTRUCTIONS:\n{chunk}\n"
        )
        raw = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are QAgenie, a thorough QA assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1200
        ).choices[0].message.content.strip()

        # ----- Parse JSON exactly like your old logic -----
        try:
            cases = json.loads(raw)
        except Exception:
            m = re.search(r'\[.*\]', raw, re.DOTALL)
            if not m:
                # save raw so we can see what went wrong
                with open(f"data/test_cases/debug_raw/chunk{idx}_BAD.txt", "w", encoding="utf-8") as f:
                    f.write(raw)
                raise ValueError(f"❌ LLM did not return valid JSON for chunk {idx}. Raw saved.")
            cases = json.loads(m.group(0))

        # ----- Save per‑chunk JSON / MD -----
        os.makedirs("data/test_cases", exist_ok=True)
        json.dump(cases, open(f"data/test_cases/test_cases_{idx}.json", "w", encoding="utf-8"), indent=2)

        md = []
        for c in cases:
            md.append(f"### {c['title']}")
            md.append("**Steps:**")
            md.extend([f"{i+1}. {s}" for i, s in enumerate(c["steps"])])
            md.append(f"**Expected Result:** {c.get('expected_result','')}\n")
        md_text = "\n".join(md)
        open(f"data/test_cases/test_cases_{idx}.md", "w", encoding="utf-8").write(md_text)

        all_cases.extend(cases)
        md_chunks.append(md_text)

    # combined
    json.dump(all_cases, open("data/test_cases/test_cases.json", "w", encoding="utf-8"), indent=2)
    open("data/test_cases/test_cases_combined.md", "w", encoding="utf-8").write("\n".join(md_chunks))
    return all_cases, md_chunks
