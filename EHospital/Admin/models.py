from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime
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


class Insurance(models.Model):
    plan_name = models.CharField(max_length=200, null=False)
    provider = models.CharField(max_length=200, null=False)
    coverage_details = models.TextField(null=True)
    monthly_premium = models.DecimalField(max_digits=10, decimal_places=2)
    annual_deductible = models.DecimalField(max_digits=10, decimal_places=2)
    coverage_limit = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    insurance_number = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"{self.plan_name}"
    

# models.py



class BillingDetail(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, null=True, blank=True)  # Phone number (optional)
    address = models.TextField(null=True, blank=True)  # Main address (optional)
    
    # Country and Zip Code (For international billing details)
    country = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    
    # Payment Details
    payment_status = models.CharField(max_length=50,       
        choices=[
            ('Pending', 'Pending'),
            ('Completed', 'Completed'),
            ('Cancelled', 'Cancelled')
        ],
         default='Pending')
    payment_method = models.CharField(max_length=50)  # e.g., Net Banking, Cash, Debit Card, UPI
    
    # Card Details (optional depending on payment method)
    card_number = models.CharField(max_length=16, null=True, blank=True)
    card_expiry = models.CharField(max_length=5, null=True, blank=True)  # MM/YY format
    card_cvv = models.CharField(max_length=3, null=True, blank=True)
    upi_id = models.CharField(max_length=50, null=True, blank=True)
    
    # Additional Fields
    transaction_id = models.CharField(max_length=100, null=True, blank=True, unique=True)  # Transaction ID
    payment_date = models.DateTimeField(null=True, blank=True, default=datetime.now)  # Date of payment (default to now)
    

    # A method to generate a unique transaction ID if not manually provided
    def save(self, *args, **kwargs):
        if not self.transaction_id:  # Generate transaction ID if not manually set
            self.transaction_id = str(uuid.uuid4())
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Billing Detail for {self.full_name}"


class OrderDetail(models.Model):
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE)
    billing_detail = models.ForeignKey(BillingDetail, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    payment_intent_id = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"Order for {self.billing_detail.full_name} - {self.insurance.plan_name}"