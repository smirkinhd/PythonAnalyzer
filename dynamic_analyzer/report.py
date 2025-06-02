import json

def generate_report(data, file="dynamic_report.json"):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
