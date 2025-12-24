RECOMMENDATION_MAP = {
    "medical_claims": "Avoid medical or health claims unless explicitly approved by the platform.",
    "financial_claims": "Avoid income, profit, or financial outcome claims.",
    "guarantees": "Remove guarantees and absolute language.",
    "personal_attributes": "Avoid referencing personal attributes or conditions."
}

def generate_recommendations(flags):
    seen = set()
    recommendations = []

    for flag in flags:
        rule = flag["type"]
        if rule not in seen:
            recommendations.append(RECOMMENDATION_MAP.get(rule))
            seen.add(rule)

    return recommendations
