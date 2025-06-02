import json

def generate_report(filename, inline_scripts, external_scripts, findings):
    return {
        "file": filename,
        "inline_scripts_detected": len(inline_scripts),
        "external_scripts": external_scripts,
        "malicious_findings": findings,
    }

def save_report(report_data, out_path="scan_report.json"):
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(report_data, f, indent=4, ensure_ascii=False)
