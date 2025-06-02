import sys
from analyzer import analyze_file

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py path/to/file.html")
        sys.exit(1)

    report = analyze_file(sys.argv[1])
    print(f"✔ Report saved to 'scan_report.json'")
    print(f"Detected: {len(report['malicious_findings'])} suspicious patterns")
