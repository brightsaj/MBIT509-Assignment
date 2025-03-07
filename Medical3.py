class ExpertSystem:
    def _init_(self):
        self.knowledge_base = {
            "Common Cold": {"cough", "sneezing", "sore throat", "runny nose", "mild fever"},
            "Flu": {"fever", "chills", "body ache", "fatigue", "cough"},
            "Malaria": {"fever", "chills", "sweating", "headache", "nausea"},
            "Typhoid": {"fever", "abdominal pain", "weakness", "loss of appetite", "headache"},
            "COVID-19": {"fever", "cough", "shortness of breath", "fatigue", "loss of taste or smell"}
        }

    def diagnose(self, symptoms):
        possible_diseases = {}
        for disease, disease_symptoms in self.knowledge_base.items():
            match_count = len(symptoms & disease_symptoms)
            if match_count > 0:
                possible_diseases[disease] = match_count

        if not possible_diseases:
            return "No matching disease found. Please consult a doctor."

        sorted_diseases = sorted(possible_diseases.items(), key=lambda x: x[1], reverse=True)
        return f"Possible diagnosis: {sorted_diseases[0][0]} (Match: {sorted_diseases[0][1]} symptoms)"


def diagnose_symptoms():
    user_input = entry.get()
    symptoms = set(map(str.strip, user_input.lower().split(",")))
    expert_system = ExpertSystem()
    diagnosis = expert_system.diagnose(symptoms)
    messagebox.showinfo("Diagnosis Result", diagnosis)


# GUI Interface
root = tkinter.Tk()
root.title("AI Expert System - Disease Diagnosis")
root.geometry("400x250")

tkinter.Label(root, text="Enter symptoms separated by commas:").pack(pady=10)
entry = tkinter.Entry(root, width=50)
entry.pack(pady=5)

tkinter.Button(root, text="Diagnose", command=diagnose_symptoms).pack(pady=20)

root.mainloop()