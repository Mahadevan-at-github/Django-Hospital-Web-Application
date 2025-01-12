from django.db import models

# Create your models here.


class AdminPatientTable(models.Model):
    username = models.CharField(max_length=200,null=False)
    f_name = models.CharField(max_length=200, null=False)
    l_name = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length=200, null=False)
    contact = models.CharField(max_length=10, null=True)
    password = models.CharField(max_length=200,null=False)
    password2 = models.CharField(max_length=200,null=False)


    def __str__(self):
        return '{}'.format(self.username)
    

class AdminDoctorTable(models.Model):
    username = models.CharField(max_length=200,null=False)
    f_name = models.CharField(max_length=200, null=False)
    l_name = models.CharField(max_length=200, null=False)
    department = models.CharField(max_length=200,null=False,default='department')
    email = models.CharField(max_length=200, null=False)
    contact = models.CharField(max_length=10, null=True)
    password = models.CharField(max_length=200,null=False)
    password2 = models.CharField(max_length=200,null=False)

    image= models.ImageField(upload_to='Hospital_media')


    def __str__(self):
        return '{}'.format(self.username)
    

class ContactTable(models.Model):
    name = models.CharField(max_length=200,null=False)
    email = models.CharField(max_length=200, null=False)
    subject = models.CharField(max_length=10, null=True)
    message = models.CharField(max_length=2000, null=True)
    

    def __str__(self):
        return '{}'.format(self.name)



class LoginTable(models.Model):
    username = models.CharField(max_length=200,null=False)
    password = models.CharField(max_length=200,null=False)
    password2 = models.CharField(max_length=200,null=False)
    type = models.CharField(max_length=200)



    def __str__(self):
        return '{}'.format(self.username)