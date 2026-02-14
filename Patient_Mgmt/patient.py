# patient.py


class Patient:
    # Intializes these values 
    def __init__(self, patient_id, name, age, condition=""):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.condition = condition

    def __str__(self):
        # print using patient_id and name 
        return f"{self.patient_id} - {self.name},\
              {self.age} yrs ({self.condition})"
