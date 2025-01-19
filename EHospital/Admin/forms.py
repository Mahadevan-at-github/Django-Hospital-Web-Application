from django import forms

from Admin.models import BillingDetail, ContactTable, Insurance
from Doctor.models import BlogPosting, Prescription
from Patient.models import Appointments


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = ['patient', 'doctor', 'appointment_date']
        widgets = {
            'patient': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 100%; height: 50px;',
                'placeholder': 'Enter Your Name'
            }),
            'doctor': forms.Select(attrs={
                'class': 'form-control select-doctor',
                'style': 'width: 100%; height: 50px;',
                'placeholder': '---Select Doctor---'
            }),
            'appointment_date': forms.DateTimeInput(attrs={
                'class': 'form-control datetimepicker',
                'type': 'datetime-local',
                'style': 'width: 100%; height: 50px;',
                'placeholder': 'Select appointment date and time'
            }),
        }

class ScheduleForm(forms.ModelForm):

    class Meta:
        model = Appointments
        fields = ['status']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control',
                'style': 'width: 100%; height: 50px;',
                'placeholder': '---Schedule---'},choices=Appointments._meta.get_field('status').choices)
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactTable
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 100%; height: 50px;',
                'placeholder': 'Enter Your Name'
            }),       
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 100%; height: 50px;',
                'placeholder': 'Enter Your Email'
            }),            
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 100%; height: 50px;',
                'placeholder': 'Enter Your Subject'
            }),            
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'width: 100%;',
                'placeholder': 'Enter Your Message'
            }),            
        }


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['medication', 'dosage','instructions']
        widgets = {      
            'medication': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 100%; height: 50px;',
                'placeholder': 'Medication'
            }),            
            'dosage': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 100%; height: 50px;',
                'placeholder': 'Dosage'
            }),            
            'instructions': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'width: 100%;',
                'placeholder': 'Enter Instructions'
            }),            
        }


class BlogForm(forms.ModelForm):

    class Meta:

        model = BlogPosting
        fields = ['title','description','content','image']

        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Description'}),
            'content': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Content'}),
        }



class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance
        fields = '__all__'
        widgets = {
            'plan_name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 100%; height: 50px;',
                'placeholder': 'Enter Plan Name'
            }),
            'provider': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 100%; height: 50px;',
                'placeholder': 'Enter Provider'
            }),
            'coverage_details': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'width: 100%; height: 100px;',
                'placeholder': 'Enter details'
            }),
            'monthly_premium': forms.NumberInput(attrs={
                'class': 'form-control',
                'style': 'width: 100%; height: 50px;',
                'placeholder': 'Enter monthly premium'
            }),
            'annual_deductible': forms.NumberInput(attrs={
                'class': 'form-control',
                'style': 'width: 100%; height: 50px;',
                'placeholder': 'Enter annual deductible'
            }),
            'coverage_limit': forms.NumberInput(attrs={
                'class': 'form-control',
                'style': 'width: 100%; height: 50px;',
                'placeholder': 'Enter coverage limit'
            }),
            'insurance_number': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 100%; height: 50px;',
                'placeholder': 'Enter insurance number'
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'form-control datepicker',
                'type': 'date',
                'style': 'width: 100%; height: 50px;',
                'placeholder': 'Select appointment date and time'
            }),
            'end_date': forms.DateInput(attrs={
                'class': 'form-control datepicker',
                'type': 'date',
                'style': 'width: 100%; height: 50px;',
                'placeholder': 'Select appointment date and time'
            }),
        }

class BillingDetailForm(forms.ModelForm):
    class Meta:
        model = BillingDetail
        fields = ['full_name', 'email', 'address', 'country', 'phone_number', 'zip_code',]
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 100%; height: 50px;',
                'placeholder': 'Enter Full Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'style': 'width: 100%; height: 50px;',
                'placeholder': 'Enter Provider'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'width: 100%; height: 100px;',
                'placeholder': 'Enter details'
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 100%; height: 50px;',
                'placeholder': 'Enter Full Name'
            }),
            'phone_number': forms.NumberInput(attrs={
                'class': 'form-control',
                'style': 'width: 100%; height: 50px;',
                'placeholder': 'Enter Phone Number'
            }),

            'zip_code': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 100%; height: 50px;',
                'placeholder': 'Enter Full Name'
            }),
        }


class PaymentStatusForm(forms.ModelForm):

    class Meta:
        model = BillingDetail
        fields = ['payment_status']
        widgets = {
            'payment_status': forms.Select(attrs={'class': 'form-control',
                'style': 'width: 100%; height: 50px;',
                'placeholder': '---Pending---'},choices=Appointments._meta.get_field('status').choices)
        }




