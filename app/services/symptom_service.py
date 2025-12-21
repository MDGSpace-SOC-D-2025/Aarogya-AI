# app/services/symptom_service.py

from app.rag.generation_service import generate_answer

def analyze_symptoms(user_input: str):
    """
    Main service function for symptom analysis.
    Currently just calls RAG pipeline.
    TODO: Add Agent-1 (Gemini interrogation) for query refinement
    """
    answer = generate_answer(user_input)
    
    return {
        "answer": answer,
        "disclaimer": "This is not a medical diagnosis. Consult a healthcare professional."
    }