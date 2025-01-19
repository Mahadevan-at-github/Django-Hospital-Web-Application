from django.db import models

from Admin.models import AdminDoctorTable

# Create your models here.

class Appointments(models.Model):
    patient = models.CharField(max_length=200)
    doctor = models.ForeignKey(AdminDoctorTable, on_delete=models.CASCADE, related_name='doctor_appointments')
    appointment_date = models.DateTimeField()
    status = models.CharField(
        max_length=50,
        choices=[
            ('Scheduled', 'Scheduled'),
            ('Completed', 'Completed'),
            ('Cancelled', 'Cancelled')
        ],
        default='Scheduled'
    )

    def __str__(self):
        return f'Appointment with {self.doctor} on {self.appointment_date}'

