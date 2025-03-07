# Knowledge Base
knowledge_base = {
    "Common Cold": ["cough", "sore throat", "runny nose", "sneezing", "fatigue"],
    "Flu": ["fever", "cough", "sore throat", "body aches", "headache", "fatigue"],
    "Allergies": ["sneezing", "itchy eyes", "runny nose", "rash"],
    "Migraine": ["headache", "nausea", "sensitivity to light", "sensitivity to sound"],
    "Stomach Flu": ["nausea", "vomiting", "diarrhea", "stomach cramps"]
}


### Step 2: Inference Mechanism

## We'll create a function that takes the user's symptoms and compares them against the knowledge base to find the most likely disease.

## python
def diagnose(symptoms):
    possible_diseases = {}
    for disease, disease_symptoms in knowledge_base.items():
        # Count how many symptoms match
        match_count = sum(symptom in disease_symptoms for symptom in symptoms)
        if match_count > 0:
            possible_diseases[disease] = match_count

    # Sort diseases by the number of matching symptoms
    sorted_diseases = sorted(possible_diseases.items(), key=lambda x: x[1], reverse=True)
    return sorted_diseases


### Step 3: User Interface

## We'll create a simple command-line interface where users can input their symptoms and receive a diagnosis.

## python
def main():
    print("Welcome to the AI Disease Diagnoser!")
    print("Please enter your symptoms separated by commas (e.g., cough, fever):")
    user_input = input().strip().lower()
    symptoms = [symptom.strip() for symptom in user_input.split(",")]

    possible_diseases = diagnose(symptoms)

    if possible_diseases:
        print("\nBased on your symptoms, you might have:")
        for disease, match_count in possible_diseases:
            print(f"- {disease} (matches {match_count} symptoms)")
    else:
        print("\nNo matching diseases found based on the symptoms provided.")

if __name__ == "__main__":
    main()