from django.db import models
from Admin.models import AdminDoctorTable
from Patient.models import Appointments

# Create your models here.

class Prescription(models.Model):
    appointment = models.OneToOneField(Appointments, on_delete=models.CASCADE, related_name='prescription')
    medication = models.TextField()
    dosage = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return f"Prescription for {self.appointment.patient} at {self.appointment.appointment_date}"


class BlogPosting(models.Model):

    title = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=200, null=True)
    content = models.CharField(max_length=500)
    comment = models.CharField(max_length=300)
    image = models.ImageField(upload_to='blog_media')


    user = models.ForeignKey(AdminDoctorTable,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return '{}'.format(self.title)