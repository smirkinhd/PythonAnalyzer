MALICIOUS_PATTERNS = [
    r"eval\(",
    r"document\.write\(",
    r"new Function\(",
    r"setTimeout\(['\"]",
    r"atob\(",
    r"unescape\(",
    r"fromCharCode",
    r"<script[^>]*src=[^>]+>",
]
