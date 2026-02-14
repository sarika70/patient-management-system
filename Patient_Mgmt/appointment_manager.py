# appointment_manager.py
from exceptions import (
    DoubleBookingError,
    AppointmentCapacityError,
    PatientNotFoundError,
    AppointmentNotFoundError
)
from exceptions import * # impot only thos functionalities need in the current module

 # import this file 

class AppointmentManager:
    # Create a dict object with 
    def __init__(self):
        self.patients = {}      # patient_id -> Patient object
        self.appointments = {}  # appointment_id -> Appointment object
        
        
    def add_patient(self, patient):
        # add patient to the patients of the Appointment Manager 
        self.patients[patient.patient_id] = patient

    def add_appointment(self, appointment):
        # add the appointment o the dict and add the object
        self.appointments[appointment.appointment_id] = appointment

    def assign_patient(self, patient_id, appointment_id):
        # check for patient_id and appointment_id 
        # check with dict object
        # raise an exception 
        if patient_id not in self.patients:
            raise PatientNotFoundError("Patient not found")
        if appointment_id not in self.appointments:
            raise AppointmentNotFoundError("Appointment not found")

        appointment = self.appointments[appointment_id]

        if len(appointment.patients) >= appointment.capacity:
            raise AppointmentCapacityError("Appointment is full")

        if patient_id in appointment.patients:
            raise DoubleBookingError("Patient already booked in this appointment")

        appointment.patients.append(patient_id)

    def list_patients(self):
        return list(self.patients.values())

    def list_appointments(self):
        return list(self.appointments.values())
