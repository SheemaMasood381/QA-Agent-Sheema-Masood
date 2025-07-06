import json
import os

def json_to_playwright_tests(json_path, ts_path):
    with open(json_path, "r", encoding="utf-8") as f:
        cases = json.load(f)

    with open(ts_path, "w", encoding="utf-8") as f:
        f.write('import { test, expect } from "@playwright/test";\n\n')

        for idx, case in enumerate(cases):
            title = case.get("title") or f"Test Case {idx+1}"
            steps = case.get("steps", [])

            # Add unique test titles to avoid duplication error
            safe_title = title.replace('"', '\\"')
            f.write(f'test("TC{idx+1}: {safe_title}", async ({{ page }}) => {{\n')
            f.write('  await page.goto("https://recruter.ai");\n\n')

            for step in steps:
                if isinstance(step, str):
                    f.write(f'  // Step: {step}\n')
                elif isinstance(step, dict):
                    action = step.get("action", "").lower()
                    selector = step.get("locator") or step.get("selector") or ""
                    value = step.get("value", "")
                    expected = step.get("expected", "")

                    if action == "fill":
                        f.write(f'  await page.fill("{selector}", "{value}");\n')
                    elif action == "click":
                        f.write(f'  await page.click("{selector}");\n')
                    elif action == "check":
                        f.write(f'  await page.check("{selector}");\n')
                    elif action == "waitforselector":
                        f.write(f'  await page.waitForSelector("{selector}");\n')
                    elif action == "assert" and expected:
                        f.write(f'  await expect(page.locator("{selector}")).toContainText("{expected}");\n')
                    else:
                        f.write(f'  // Unknown structured step: {step}\n')
                else:
                    f.write(f'  // Unrecognized step format: {step}\n')

            if case.get("expected_result"):
                f.write(f'\n  // Expected Result: {case["expected_result"]}\n')

            f.write('});\n\n')
