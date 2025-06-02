from html_parser import extract_scripts
from js_analyzer import analyze_js
from report import generate_report, save_report

def analyze_file(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    inline_scripts, external_scripts = extract_scripts(html)
    findings = []

    for script in inline_scripts:
        findings.extend(analyze_js(script))

    report = generate_report(html_path, inline_scripts, external_scripts, findings)
    save_report(report)
    return report
