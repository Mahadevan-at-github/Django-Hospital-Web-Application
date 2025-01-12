from django.contrib import admin
from .models import AdminPatientTable,AdminDoctorTable,LoginTable,ContactTable
from Patient.models import Appointments 
from Doctor.models import Prescription,BlogPosting
# Register your models here.

admin.site.register(AdminPatientTable)
admin.site.register(AdminDoctorTable)
admin.site.register(LoginTable)
admin.site.register(Appointments)
admin.site.register(ContactTable)
admin.site.register(Prescription)
admin.site.register(BlogPosting)
