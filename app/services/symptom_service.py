from app.data.symptom_data import SYMPTOM_DB

def analyze_symptoms(text: str):
    text = text.lower()

    for symptom, info in SYMPTOM_DB.items():
        if symptom in text:
            return {
                "detected_symptoms": symptom,
                "possible_causes": info["possible_causes"],
                "recommended_doctor": info["doctor"],
                "self_care_tips": info["self_care"],
                "disclaimer": "This is not a medical diagnosis."
            }

    return {
        "detected_symptoms": "unknown",
        "possible_causes": [],
        "recommended_doctor": "General Physician",
        "self_care_tips": [],
        "disclaimer": "This is not a medical diagnosis."
    }
