RISK_RULES = {
    "medical_claims": {
        "weight": 30,
        "keywords": [
            "cure", "treat", "heal", "diagnose", "medical",
            "doctor approved", "clinically proven"
        ]
    },
    "financial_claims": {
        "weight": 25,
        "keywords": [
            "make money", "earn", "profit", "income", "get rich"
        ]
    },
    "guarantees": {
        "weight": 20,
        "keywords": [
            "guaranteed", "100%", "instant results", "no risk"
        ]
    },
    "personal_attributes": {
        "weight": 15,
        "keywords": [
            "you are", "your condition", "suffering from",
            "struggling with", "overweight", "broke"
        ]
    }
}

SENSITIVE_CATEGORIES = {
    "health": 1.3,
    "weight_loss": 1.4,
    "finance": 1.3,
    "general": 1.0
}
