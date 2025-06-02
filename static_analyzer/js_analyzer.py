import re
from signatures import MALICIOUS_PATTERNS

def analyze_js(js_code: str):
    matches = []
    for pattern in MALICIOUS_PATTERNS:
        for match in re.finditer(pattern, js_code):
            matches.append({
                "pattern": pattern,
                "snippet": js_code[max(0, match.start() - 30):match.end() + 30]
            })
    return matches
