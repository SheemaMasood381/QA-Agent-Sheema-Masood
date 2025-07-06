# QAAgent Task – Sheema Masood

## Overview

This repository contains the solution for the **QA AGENT** coding task, assigned as part of a technical job evaluation. The objective was to build an AI-powered multi-tool QA agent that automates end-to-end frontend test case generation, execution, and reporting for [Recruter.ai](https://recruter.ai), using a "How To" YouTube video and/or help documentation as the basis for QA coverage.

---

## Features

### 🧩 Test Case Generator Agent (RAG + LLM)
- Extracts and transcribes instructional videos (YouTube/Whisper)
- Optionally ingests help documentation
- Generates comprehensive frontend test cases:
  - Core user flows
  - Edge cases & error handling
  - Cross-browser & mobile variants
  - Accessibility & performance checks
- Outputs test cases in:
  - JSON (for automation)
  - Markdown (for human readability)

### 🧩 Automated Test Execution Agent
- Converts generated test cases into Playwright scripts
- Executes tests against Recruter.ai (local/staging)
- Captures results, screenshots, and logs

### 📊 Reporting & Dashboard
- Streamlit dashboard displays:
  - Test case generation history (sidebar)
  - Test execution summaries (pass/fail, duration)
  - Downloadable artifacts (JSON, Markdown, logs, screenshots)

### 🚀 CI/CD Integration
- GitHub Actions workflow for automated test runs and artifact uploads

---

## How It Works

1. **Ingest Data**  
   - Transcribes a YouTube "how-to" video or reads help docs

2. **Generate Test Cases**  
   - Uses LLM (e.g., GPT-4o) to create detailed and structured frontend test cases

3. **Convert to Playwright Scripts**  
   - Auto-generates Playwright-compatible test scripts

4. **Execute & Report**  
   - Runs tests, collects pass/fail results, screenshots, and logs  
   - Results and history are viewable/downloadable from the Streamlit dashboard

---

## Quickstart

1. **Clone the repository**
2. **Install dependencies**  
   - Python: `pip install -r requirements.txt`  
   - Node.js: `npm ci`  
   - Playwright: `npx playwright install --with-deps`
3. **Run the Streamlit app**  
   ```bash
   streamlit run app.py
   ```
4. **Trigger test case generation** with your chosen YouTube link or help doc  
5. **Execute tests** and view results on the dashboard

---

## Repository Structure

- `src/` – Core agent source code (data ingestion, test case generation, script conversion, etc.)
- `app.py` – Streamlit dashboard application
- `tests/` – Playwright test scripts (auto-generated)
- `data/` – Transcripts, generated test cases, results, logs, and screenshots
- `.github/workflows/ci.yml` – GitHub Actions workflow for CI/CD

---

## About

**This project was assigned as a technical evaluation for a QA engineering position.**  
Developed by [Sheema Masood](https://www.linkedin.com/in/sheema-masood/)  
- [GitHub](https://github.com/sheemamasood381/)

---

## License

This repository is for job evaluation and demonstration purposes only.