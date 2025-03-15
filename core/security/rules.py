# core/security/rules.py
import re

def check_sql_injection(code: str) -> list:
    patterns = [
        r"execute\s*\(\s*[\'\"].*?\%s.*?[\'\"].*?,\s*.*?\)",
        r"cursor\.execute\s*\(\s*[\'\"].*?\s*\+\s*.*?[\'\"].*?\)"
    ]
    issues = []
    for pattern in patterns:
        matches = re.finditer(pattern, code)
        for match in matches:
            issues.append({
                "type": "security",
                "severity": "high",
                "message": "Potential SQL injection vulnerability",
                "line": code[:match.start()].count('\n') + 1
            })
    return issues
