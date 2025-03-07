### Solution Code
# Define the knowledge base of diseases and their symptoms
knowledge_base = {
    'Common Cold': ['cough', 'sore throat', 'runny nose', 'sneezing', 'congestion'],
    'Flu': ['fever', 'muscle aches', 'fatigue', 'cough', 'headache', 'sore throat', 'chills'],
    'Allergy': ['sneezing', 'itchy eyes', 'runny nose', 'congestion'],
    'Strep Throat': ['sore throat', 'fever', 'swollen tonsils', 'difficulty swallowing'],
    'Migraine': ['headache', 'nausea', 'sensitivity to light', 'sensitivity to sound'],
    'Gastroenteritis': ['diarrhea', 'nausea', 'vomiting', 'stomach cramps', 'fever'],
    'Pneumonia': ['cough', 'fever', 'chest pain', 'shortness of breath', 'fatigue']
}

# Collect all unique symptoms from the knowledge base
all_symptoms = sorted(list({symptom for symptoms in knowledge_base.values() for symptom in symptoms}))

# Display available symptoms to the user
print("Please select the symptoms you are experiencing from the list below:")
for idx, symptom in enumerate(all_symptoms, 1):
    print(f"{idx}. {symptom}")

# Get user input for symptoms
selected_numbers = input("\nEnter the numbers of your symptoms separated by commas: ").strip().split(',')

# Process the input to get user symptoms
user_symptoms = []
for num in selected_numbers:
    num = num.strip()
    if not num:
        continue
    try:
        index = int(num) - 1  # Convert to 0-based index
        if 0 <= index < len(all_symptoms):
            user_symptoms.append(all_symptoms[index])
        else:
            print(f"Warning: {num} is an invalid option and will be skipped.")
    except ValueError:
        print(f"Warning: '{num}' is not a valid number and will be skipped.")

# Calculate possible diseases based on symptoms
possible_diseases = []
for disease, symptoms in knowledge_base.items():
    matches = set(symptoms) & set(user_symptoms)
    score = len(matches)
    total_symptoms = len(symptoms)
    ratio = score / total_symptoms if total_symptoms > 0 else 0
    possible_diseases.append((disease, score, total_symptoms, ratio))

# Sort by score (descending) and then by ratio (descending)
possible_diseases.sort(key=lambda x: (-x[1], -x[3]))

# Display results
print("\nPossible conditions based on your symptoms:")
found = False
for disease, score, total, ratio in possible_diseases:
    if score > 0:
        print(f"- {disease}: {score} out of {total} symptoms matched ({ratio:.0%})")
        found = True
if not found:
    print("No matching conditions found based on the symptoms provided.")

# Disclaimer
print("\nNote: This tool is for informational purposes only and is not a substitute for professional medical advice.")
