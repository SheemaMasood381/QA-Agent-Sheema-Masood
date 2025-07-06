import subprocess, os, shutil
import json

def run_playwright_tests(script_path, results_dir="results"):
    import os, subprocess
    os.makedirs(results_dir, exist_ok=True)
    # Remove --reporter argument!
    cmd = f'npx playwright test "{script_path}"'
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    with open(os.path.join(results_dir, "stdout.log"), "w", encoding="utf-8") as f:
        f.write(result.stdout)
    with open(os.path.join(results_dir, "stderr.log"), "w", encoding="utf-8") as f:
        f.write(result.stderr)
    return result

def parse_test_results(results_dir="results"):
    report_file = os.path.join(results_dir, "test-results.json")
    if not os.path.exists(report_file):
        return {
            "total": 0,
            "passed": 0,
            "failed": 0,
            "skipped": 0,
            "status_message": "⚠️ No tests executed."
        }

    with open(report_file, encoding="utf-8") as f:
        data = json.load(f)

    # Stats block (Playwright 1.53+)
    stats = data.get("stats", {})
    total = stats.get("expected", 0) + stats.get("unexpected", 0) + stats.get("skipped", 0)
    passed = stats.get("expected", 0)
    failed = stats.get("unexpected", 0)
    skipped = stats.get("skipped", 0)
    duration = stats.get("duration", 0)

    summary = {
        "total": total,
        "passed": passed,
        "failed": failed,
        "skipped": skipped,
        "duration_seconds": round(duration/1000, 1),
        "status_message": (
            "🎉 All tests passed!" if failed == 0 and total > 0
            else "❌ Some tests failed." if failed > 0
            else "⚠️ No tests executed."
        )
    }
    return summary