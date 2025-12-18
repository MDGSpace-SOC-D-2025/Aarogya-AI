from pydantic import BaseModel

class SymptomRequest(BaseModel):
    symptoms: str

class SymptomResponse(BaseModel):
    detected_symptoms: str
    possible_causes: list[str]
    recommended_doctor: str
    self_care_tips: list[str]
    disclaimer: str

