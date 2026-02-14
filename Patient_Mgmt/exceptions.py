# exceptions.py
class DoubleBookingError(Exception):
    pass

class AppointmentCapacityError(Exception):
    pass

class PatientNotFoundError(Exception):
    pass

class AppointmentNotFoundError(Exception):
    pass
