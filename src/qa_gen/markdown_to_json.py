import re, json

# --------------------------------------------
#  Helper functions
# --------------------------------------------
def detect_action(step_str):
    s = step_str.lower()
    if any(k in s for k in ["enter", "type", "fill"]):
        return "fill"
    if any(k in s for k in ["click", "press", "select"]):
        return "click"
    if "verify" in s or "check" in s or "expect" in s:
        return "expect_text"
    if "navigate" in s or "go to" in s:
        return "goto"
    return "comment"

def default_selector(step_str):
    # Minimal heuristic mapping — adjust as needed
    s = step_str.lower()
    if "job description" in s:
        return "input[name='jobDescription']"
    if "save" in s:
        return "button:has-text('Save')"
    if "skills" in s:
        return "#skills-list"
    if "difficulty" in s:
        return "#difficulty-level-select"
    if "avatar" in s:
        return "#ai-avatar-select"
    if "create interview" in s:
        return "#create-interview-button"
    return "#todo‑selector"

def from_markdown(md_text:str):
    """Convert your Markdown preview into structured JSON."""
    lines = [l.strip() for l in md_text.splitlines() if l.strip()]
    cases, cur = [], None

    for ln in lines:
        # ---------- New test title ----------
        if not ln.startswith("{") and not ln.startswith("'") and "Steps:" not in ln and "Expected Result:" not in ln:
            # save previous
            if cur:
                cases.append(cur)
            cur = {"title": ln, "steps": [], "expected_result": ""}
            continue

        # ---------- Step dict ----------
        if ln.startswith("{"):
            try:
                d = eval(ln)               # input comes from your own LLM, relatively safe
                action = detect_action(d.get("step",""))
                selector = default_selector(d.get("step",""))
                value = d.get("input","")
                cur["steps"].append({"action": action, "selector": selector, "value": value})
            except Exception as e:
                cur["steps"].append({"action": "comment", "value": f"UNPARSED: {ln}"})
            continue

        # ---------- Expected Result ----------
        if "Expected Result:" in ln:
            cur["expected_result"] = ln.split("Expected Result:")[1].strip()

    if cur: cases.append(cur)
    return cases
