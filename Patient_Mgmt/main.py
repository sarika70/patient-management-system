# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 06:45:09 2025

@author: mjayant
"""

# main.py
from patient import Patient
from appointment import Appointment
from appointment_manager import AppointmentManager
from report import patient_report, appointment_report

def main():
    manager = AppointmentManager()

    while True:
        print("\nPatient & Appointment Management")
        print("1. Add Patient")
        print("2. Add Appointment")
        print("3. Assign Patient to Appointment")
        print("4. View Patients")
        print("5. View Appointments")
        print("6. Reports")
        print("7. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            pid = input("Patient ID: ")
            name = input("Name: ")
            age = int(input("Age: "))
            cond = input("Condition: ")
            manager.add_patient(Patient(pid, name, age, cond))
            print("Patient added.")

        elif choice == "2":
            aid = input("Appointment ID: ")
            doc = input("Doctor: ")
            date = input("Date (YYYY-MM-DD): ")
            slot = input("Time Slot (e.g. 09:00-09:30): ")
            cap = int(input("Capacity: "))
            manager.add_appointment(Appointment(aid, doc, date, slot, cap))
            print("Appointment added.")

        elif choice == "3":
            pid = input("Patient ID: ")
            aid = input("Appointment ID: ")
            try:
                manager.assign_patient(pid, aid)
                print("Assigned successfully.")
            except Exception as e:
                print("Error:", e)

        elif choice == "4":
            for p in manager.list_patients():
                print("-", p)

        elif choice == "5":
            for a in manager.list_appointments():
                print("-", a)

        elif choice == "6":
            sub = input("Report type (p=patient / a=appointment): ")
            if sub == "p":
                pid = input("Patient ID: ")
                print(patient_report(manager, pid))
            else:
                aid = input("Appointment ID: ")
                print(appointment_report(manager, aid))

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
