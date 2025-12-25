def determine_specialization(symptoms: str, severity: str) -> str:
    """
    Maps symptoms to doctor specialization.
    
    How it works:
    - Takes refined symptoms (like "chest pain, shortness of breath")
    - Checks for keywords
    - Returns the type of doctor needed
    
    Args:
        symptoms: The refined symptoms from Agent-1
        severity: MILD/MODERATE/SEVERE from Agent-2
    
    Returns:
        String like "Cardiologist" or "General Physician"
    """
    
    # Convert to lowercase for easier matching
    symptoms_lower = symptoms.lower()
    
    # Check for heart-related symptoms
    if any(word in symptoms_lower for word in ['chest pain', 'heart', 'cardiac']):
        return "Cardiologist"
    
    # Check for skin-related symptoms
    elif any(word in symptoms_lower for word in ['skin', 'rash', 'acne', 'itching']):
        return "Dermatologist"
    
    # Check for ear/nose/throat symptoms
    elif any(word in symptoms_lower for word in ['ear', 'nose', 'throat', 'sore throat']):
        return "ENT Specialist"
    
    # Check for bone/joint symptoms
    elif any(word in symptoms_lower for word in ['bone', 'joint', 'fracture', 'sprain']):
        return "Orthopedic"
    
    # Check for eye symptoms
    elif any(word in symptoms_lower for word in ['eye', 'vision', 'blurry']):
        return "Ophthalmologist"
    
    # Default case: if no specific match, use general physician
    else:
        return "General Physician"


# Test the function if running this file directly
if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("chest pain and shortness of breath", "SEVERE"),
        ("skin rash on arms", "MILD"),
        ("sore throat", "MODERATE"),
        ("fever and headache", "MODERATE")
    ]
    
    print("Testing Specialization Mapper:\n")
    for symptoms, severity in test_cases:
        result = determine_specialization(symptoms, severity)
        print(f"Symptoms: {symptoms}")
        print(f"→ Doctor needed: {result}\n")