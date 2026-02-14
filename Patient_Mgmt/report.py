# -*- coding: utf-8 -*-


# report.py
# 
# Use the appoinment manager class/object 
def patient_report(manager, patient_id):
    # 
    if patient_id not in manager.patients:
        return "Patient not found."
    patient = manager.patients[patient_id]
    lines = [f"Report for {patient.name} ({patient.patient_id}):"]
    for appt in manager.appointments.values():
        if patient_id in appt.patients:
            lines.append(f" - {appt}")
    return "\n".join(lines)

def appointment_report(manager, appointment_id):
    if appointment_id not in manager.appointments:
        return "Appointment not found."
    appt = manager.appointments[appointment_id]
    lines = [f"Report for {appt}"]
    for pid in appt.patients:
        p = manager.patients[pid]
        lines.append(f"   * {p.name}, {p.age} yrs")
    return "\n".join(lines)
