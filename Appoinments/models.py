from django.db import models

class Appoinment(models.Model):
    TIME_SLOTS = [
    ('09:00 AM - 10:00 AM', '09:00 AM - 10:00 AM'),
    ('10:00 AM - 11:00 AM', '10:00 AM - 11:00 AM'),
    ('11:00 AM - 12:00 PM', '11:00 AM - 12:00 PM'),
    ('12:00 PM - 01:00 PM', '12:00 PM - 01:00 PM'),
    ('01:00 PM - 02:00 PM', '01:00 PM - 02:00 PM'),
    ('02:00 PM - 03:00 PM', '02:00 PM - 03:00 PM'),
    ('03:00 PM - 04:00 PM', '03:00 PM - 04:00 PM'),
    ('04:00 PM - 05:00 PM', '04:00 PM - 05:00 PM'),
    ('05:00 PM - 06:00 PM', '05:00 PM - 06:00 PM')

]
    doctor_name = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    appointment_date = models.DateField()
    time_slot = models.CharField(max_length=20,choices=TIME_SLOTS)
    problem = models.TextField()

    def __str__(self):
        return f"{self.doctor_name} - {self.appointment_date}"