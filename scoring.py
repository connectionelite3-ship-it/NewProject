from app.rules import RISK_RULES, SENSITIVE_CATEGORIES

def calculate_risk(text: str, category: str):
    flags = []
    score = 0

    text = text.lower()
    multiplier = SENSITIVE_CATEGORIES.get(category, 1.0)

    for rule, config in RISK_RULES.items():
        for keyword in config["keywords"]:
            if keyword in text:
                flags.append({
                    "type": rule,
                    "keyword": keyword,
                    "weight": config["weight"]
                })
                score += config["weight"]

    score = int(score * multiplier)
    score = min(score, 100)

    if score < 30:
        risk_level = "Low"
    elif score < 60:
        risk_level = "Medium"
    else:
        risk_level = "High"

    return risk_level, score, flags
