# appointment.py

from exceptions import AppointmentCapacityError
class Appointment:
    
    def __init__(self, appointment_id, doctor, date, time_slot, capacity=1):
        # pass these paramenter to the construction
        self.appointment_id = appointment_id
        self.doctor = doctor
        self.date = date          # e.g., "2025-10-01"
        self.time_slot = time_slot  # e.g., "09:00-09:30"
        self.capacity = capacity
        self.patients = []  # store patient IDs

    
    def add_patient(self, patient_id):
        # add the patient_id and the patient object to the patients instance variable in this class
        # check for the capacity 
        if len(self.patients) >= self.capacity:
            raise Exception("Appointment is full") # 
        if patient_id in self.patients:
            raise Exception("Patient already in this appointment")
        self.patients.append(patient_id)

    
    def __str__(self):
        
        return f"[{self.appointment_id}] Dr. {self.doctor}, {self.date} {self.time_slot}, {len(self.patients)}/{self.capacity} booked"
