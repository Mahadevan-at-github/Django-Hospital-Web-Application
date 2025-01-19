
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404, render,redirect
from django.core.paginator import Paginator,EmptyPage
from Admin.forms import AppointmentForm, BillingDetailForm, BlogForm,ContactForm, InsuranceForm, ScheduleForm,PrescriptionForm,PaymentStatusForm
from Doctor.models import BlogPosting, Prescription
from .models import AdminPatientTable, BillingDetail, Insurance, LoginTable, AdminDoctorTable, OrderDetail
from Patient.models import Appointments

# Create your views here.

# ------------MAIN TEMPLATES AND FUNCTIONS-----------------



def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def feature(request):
    return render(request, 'feature.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact') 
    else:
        form = ContactForm()
    
 
    return render(request, 'maincontact.html', {'form': form})


def service(request):
    return render(request, 'service.html')

def testimonial(request):
    return render(request, 'testimonial.html')




# ------------PATIENT TEMPLATES AND FUNCTIONS-----------------

def patientbase(request):
    return render(request,'patient temp/patientbase.html')

def patienthome(request):
    return render(request, 'patient temp/index.html')

def patientabout(request):
    return render(request, 'patient temp/about.html')

def patientservice(request):
    return render(request, 'patient temp/service.html')

def patientappointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success') 
    else:
        form = AppointmentForm()
    
    return render(request, 'patient temp/appointment.html', {'form': form})


def appointmentsuccess(request):
    return render(request, 'patient temp/Success.html')


def patientfeature(request):
    return render(request, 'patient temp/feature.html')


def patientcontact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact') 
    else:
        form = ContactForm()
    
    return render(request, 'patient temp/contact.html', {'form': form})


def patientdoctor(request):
    doctors = AdminDoctorTable.objects.all()
    paginator = Paginator(doctors, 8) 

    page_number = request.GET.get('page')
    doctors = paginator.get_page(page_number)


    return render(request, 'patient temp/team.html',{'doctors': doctors})


def doctorlist(request, docid):
    doctor = AdminDoctorTable.objects.get(id=docid)
    return render(request, 'patient temp/team.html', {'doctor': doctor})


def patientblog(request):
    blogs = BlogPosting.objects.all()
    paginator = Paginator(blogs, 8) 

    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)


    return render(request, 'patient temp/patientblog.html',{'blogs': blogs})


def bloglist(request, docid):
    blog = AdminDoctorTable.objects.get(id=docid)
    return render(request, 'patient temp/patientblog.html', {'blog': blog})



# ------------DOCTOR TEMPLATES AND FUNCTIONS-----------------


def doctorbase(request):
    return render(request,'doctor temp/index.html')

def doctorhome(request):
    return render(request,'doctor temp/index.html')

def doctorabout(request):
    return render(request, 'doctor temp/about.html')

def doctorservice(request):
    return render(request, 'doctor temp/service.html')

def doctorcontact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact') 
    else:
        form = ContactForm()
    return render(request, 'doctor temp/contact.html',{'form': form})


def doctorListView(request):

    appointment = Appointments.objects.all()

    paginator = Paginator(appointment, 5)

    page_number = request.GET.get('page')

    try:
        page = paginator.get_page(page_number)
    except EmptyPage:
        page = paginator.page(page_number.num_pages)

    return render(request, 'doctor temp/detail.html', {'page':page})


def Search_Appointment(request):
    query = None
    books = None


    if 'q' in request.GET:

        query=request.GET.get('q')
        books = Appointments.objects.filter(Q(patient__icontains=query)| Q(appointment_date__icontains=query) | Q(doctor__username__icontains=query) |  # Search in the doctor's username
            Q(doctor__f_name__icontains=query) | 
            Q(doctor__l_name__icontains=query))
    else:
        books=[]

    context = {'books':books,'query':query}
    return render(request,'doctor temp/search.html',context)



def appointmentUpdate(request,appoin_id):

    appointment = Appointments.objects.get(id=appoin_id)

    if request.method=='POST':
        form = ScheduleForm(request.POST,instance=appointment)

        if form.is_valid():
            form.save()
            return redirect('doctorappointment')
    else:
        form=ScheduleForm(instance=appointment)
    return render(request,'doctor temp/appointmentupdate.html',{'form':form})


def appointmentDelete(request,appoin_id):

    appointment = Appointments.objects.get(id=appoin_id)

    if request.method=='POST':

        appointment.delete()

        return redirect('doctorappointment')

    return render(request,'doctor temp/appointmentdelete.html',{'appointment':appointment})


def prescription(request,appoin_id):

    appointment = get_object_or_404(Appointments, id=appoin_id)

    prescription = Prescription.objects.filter(appointment=appointment).first()

    if prescription:
        messages.info(request, "Prescription already exists for this appointment.")
        form = PrescriptionForm(instance=prescription)
    else:
        form = PrescriptionForm()

        
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.appointment = appointment
            prescription.save()
            return redirect('doctorappointment')
    else:
        form = PrescriptionForm()
    return render(request, 'doctor temp/prescription.html', {'form': form, 'appointment': appointment})



def prescriptionlist(request):

    prescription = Prescription.objects.all()

    paginator = Paginator(prescription, 5)

    page_number = request.GET.get('page')

    try:
        page = paginator.get_page(page_number)
    except EmptyPage:
        page = paginator.page(page_number.num_pages)
    
    return render(request, 'doctor temp/prescriptionlist.html', {'page':page})



def Prescriptiondetail(request,pre_id):

    prescription = Prescription.objects.get(id=pre_id)

    return render(request, 'doctor temp/prescriptiondetail.html', {'prescription': prescription})



def prescriptionUpdate(request,pre_id):

    prescription = Prescription.objects.get(id=pre_id)

    if request.method=='POST':
        form = PrescriptionForm(request.POST,instance=prescription)

        if form.is_valid():
            form.save()
            return redirect('doctorappointment')
    else:
        form=PrescriptionForm(instance=prescription)
    return render(request,'doctor temp/prescriptionupdate.html',{'form':form})



def prescriptionDelete(request,pre_id):

    prescription = Prescription.objects.get(id=pre_id)

    if request.method=='POST':

        prescription.delete()

        return redirect('doctorappointment')

    return render(request,'doctor temp/prescriptiondelete.html',{'prescription':prescription})


def blog(request):
    blog = BlogPosting.objects.all()

    paginator = Paginator(blog, 5)

    page_number = request.GET.get('page')

    try:
        page = paginator.get_page(page_number)
    except EmptyPage:
        page = paginator.page(page_number.num_pages)

    return render(request, 'doctor temp/blog.html', {'page':page})



def createBlog(request):
    blogs = BlogPosting.objects.all()

    form = BlogForm()

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog')

    return render(request, 'doctor temp/doctorcreateblog.html', {'form': form, 'blogs': blogs})


def Blogdetail(request,blog_id):

    blog = BlogPosting.objects.get(id=blog_id)

    return render(request, 'doctor temp/blogdetail.html', {'blog': blog})



def blogUpdate(request,blog_id):

    blog = BlogPosting.objects.get(id=blog_id)

    if request.method=='POST':
        form = BlogForm(request.POST,request.FILES,instance=blog)

        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form=BlogForm(instance=blog)

    return render(request,'doctor temp/blogupdate.html',{'form':form})



def blogdelete(request,blog_id):
        blog = BlogPosting.objects.get(id=blog_id)

        if request.method == 'POST':
            blog.delete()

            return redirect('blog')

        return render(request, 'doctor temp/blogdelete.html', {'blog': blog})




# ------------ADMIN TEMPLATES AND FUNCTIONS-----------------


def admin_view(request):

    books = AdminPatientTable.objects.all()

    paginator = Paginator(books, 5)

    page_number = request.GET.get('page')

    try:
        page = paginator.get_page(page_number)
    except EmptyPage:
        page = paginator.page(page_number.num_pages)

    return render(request,'admin temp/listview.html',{'page':page})



def detailsView(request,user_id):

    name = AdminPatientTable.objects.get(id=user_id)

    return render(request, 'admin temp/detail.html', {'name': name})


def update_user(request, user_id):
    try:
        # Retrieve the user object
        user = AdminPatientTable.objects.get(id=user_id)
    except AdminPatientTable.DoesNotExist:
        # Handle case where user does not exist
        messages.error(request, 'User not found.')
        return redirect('admin_view')  # Replace with your user list view name

    if request.method == 'POST':
        # Update fields from the form
        username = request.POST.get('username')
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')



        user.username = username
        user.f_name = f_name
        user.l_name = l_name
        user.email = email
        user.contact = contact


        user.save()

        messages.success(request, 'User updated successfully!')
        return redirect('admin_view')

    return render(request, 'admin temp/update.html', {'user': user})


def userdelete(request,user_id):
        user = AdminPatientTable.objects.get(id=user_id)

        if request.method == 'POST':
            user.delete()

            return redirect('admin_view')

        return render(request, 'admin temp/userdelete.html', {'user': user})



def adminblog(request):
    blog = BlogPosting.objects.all()

    paginator = Paginator(blog, 5)

    page_number = request.GET.get('page')

    try:
        page = paginator.get_page(page_number)
    except EmptyPage:
        page = paginator.page(page_number.num_pages)

    return render(request, 'admin temp/blogs.html', {'page':page})



def admincreateBlog(request):
    blogs = BlogPosting.objects.all()

    form = BlogForm()

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog')

    return render(request, 'admin temp/admincreateblog.html', {'form': form, 'blogs': blogs})


def adminBlogdetail(request,blog_id):

    blog = BlogPosting.objects.get(id=blog_id)

    return render(request, 'admin temp/blog_detail.html', {'blog': blog})



def adminblogUpdate(request,blog_id):

    blog = BlogPosting.objects.get(id=blog_id)

    if request.method=='POST':
        form = BlogForm(request.POST,request.FILES,instance=blog)

        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form=BlogForm(instance=blog)

    return render(request,'admin temp/blog_update.html',{'form':form})



def adminblogdelete(request,blog_id):
        blog = BlogPosting.objects.get(id=blog_id)

        if request.method == 'POST':
            blog.delete()

            return redirect('blog')

        return render(request, 'admin temp/blog_delete.html', {'blog': blog})




def adminprescriptionlist(request):

    prescription = Prescription.objects.all()

    paginator = Paginator(prescription, 5)

    page_number = request.GET.get('page')

    try:
        page = paginator.get_page(page_number)
    except EmptyPage:
        page = paginator.page(page_number.num_pages)
    
    return render(request, 'admin temp/prescription_list.html', {'page':page})



def adminPrescriptiondetail(request,pre_id):

    prescription = Prescription.objects.get(id=pre_id)

    return render(request, 'admin temp/prescription_detail.html', {'prescription': prescription})



def adminprescriptionUpdate(request,pre_id):

    prescription = Prescription.objects.get(id=pre_id)

    if request.method=='POST':
        form = PrescriptionForm(request.POST,instance=prescription)

        if form.is_valid():
            form.save()
            return redirect('prescription_list')
    else:
        form=PrescriptionForm(instance=prescription)
    return render(request,'admin temp/prescription_update.html',{'form':form})



def adminprescriptionDelete(request,pre_id):

    prescription = Prescription.objects.get(id=pre_id)

    if request.method=='POST':

        prescription.delete()

        return redirect('doctorappointment')

    return render(request,'admin temp/prescription_delete.html',{'prescription':prescription})


def appointmentView(request):

    appointment = Appointments.objects.all()

    paginator = Paginator(appointment, 5)

    page_number = request.GET.get('page')

    try:
        page = paginator.get_page(page_number)
    except EmptyPage:
        page = paginator.page(page_number.num_pages)

    return render(request, 'admin temp/appointmentdetail.html', {'page':page})



def adminappointmentUpdate(request,appoin_id):

    appointment = Appointments.objects.get(id=appoin_id)

    if request.method=='POST':
        form = ScheduleForm(request.POST,instance=appointment)

        if form.is_valid():
            form.save()
            return redirect('adminappointment')
    else:
        form=ScheduleForm(instance=appointment)
    return render(request,'admin temp/appointment_update.html',{'form':form})


def adminappointmentDelete(request,appoin_id):

    appointment = Appointments.objects.get(id=appoin_id)

    if request.method=='POST':

        appointment.delete()

        return redirect('adminappointment')

    return render(request,'admin temp/appointment_delete.html',{'appointment':appointment})



def doctor_view(request):

    books = AdminDoctorTable.objects.all()

    paginator = Paginator(books, 5)

    page_number = request.GET.get('page')

    try:
        page = paginator.get_page(page_number)
    except EmptyPage:
        page = paginator.page(page_number.num_pages)

    return render(request,'admin temp/doctorlist.html',{'page':page})



def doctorDetails(request,user_id):

    name = AdminDoctorTable.objects.get(id=user_id)

    return render(request, 'admin temp/detail.html', {'name': name})


def update_doctor(request, user_id):
    try:
        # Retrieve the user object
        user = AdminDoctorTable.objects.get(id=user_id)
    except AdminDoctorTable.DoesNotExist:
        # Handle case where user does not exist
        messages.error(request, 'User not found.')
        return redirect('doctor_view')  # Replace with your user list view name

    if request.method == 'POST':
        # Update fields from the form
        username = request.POST.get('username')
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')



        user.username = username
        user.f_name = f_name
        user.l_name = l_name
        user.email = email
        user.contact = contact


        user.save()

        messages.success(request, 'User updated successfully!')
        return redirect('doctor_view')

    return render(request, 'admin temp/update.html', {'user': user})


def doctordelete(request,user_id):
        user = AdminDoctorTable.objects.get(id=user_id)

        if request.method == 'POST':
            user.delete()

            return redirect('doctor_view')

        return render(request, 'admin temp/userdelete.html', {'user': user})






# ------------REGISTRATION TEMPLATES AND FUNCTIONS-----------------


def Registration(request):

    login_table = LoginTable()
    userprofile = AdminPatientTable()

    if request.method=='POST':

        userprofile.username=request.POST['username']
        userprofile.f_name = request.POST['f_name']
        userprofile.l_name = request.POST['l_name']
        userprofile.email = request.POST['email']
        userprofile.contact=request.POST['contact']
        userprofile.password = request.POST['password']
        userprofile.password2 = request.POST['password2']

        login_table.username = request.POST['username']
        login_table.password = request.POST['password']
        login_table.password2 = request.POST['password2']
        login_table.type='user'

        if request.POST['password']==request.POST['password2']:
            userprofile.save()
            login_table.save()

            messages.info(request,'Registration Success')
            return redirect('login')
        else:
            messages.info(request,'Password not working')
            return('cls')

    return render(request,'register form/register.html')


def DoctorRegistration(request):
    login_table = LoginTable()
    doctorprofile = AdminDoctorTable()

    if request.method=='POST':

        doctorprofile.username=request.POST['username']
        doctorprofile.f_name = request.POST['f_name']
        doctorprofile.l_name = request.POST['l_name']
        doctorprofile.email = request.POST['email']
        doctorprofile.contact=request.POST['contact']
        doctorprofile.image = request.FILES.get('image')
        doctorprofile.password = request.POST['password']
        doctorprofile.password2 = request.POST['password2']

        login_table.username = request.POST['username']
        login_table.password = request.POST['password']
        login_table.password2 = request.POST['password2']
        login_table.type='doctor'

        if request.POST['password']==request.POST['password2']:
            doctorprofile.save()
            login_table.save()

            messages.info(request,'Registration Success')
            return redirect('login')
        else:
            messages.info(request,'Password not working')
            messages.error('Password not matching')
            

    return render(request,'doctor temp/register.html')



def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user=LoginTable.objects.filter(username=username,password=password,type ='user').exists()
        doctor=LoginTable.objects.filter(username=username,password=password,type ='doctor').exists()

        try:
            if user or doctor is not None:
                user_details=LoginTable.objects.get(username=username,password=password)
                user_name = user_details.username
                type=user_details.type

                if type=='user':
                    request.session['username'] = user_name
                    return redirect('patienthome')
                elif type=='doctor':
                    request.session['username'] = user_name
                    return redirect('doctorhome')
                elif type=='admin':
                    request.session['username'] = user_name
                    return redirect("admin_view")
            else:
                messages.info(request,'Invalid Username or Password')
        except:
            messages.info(request,'Invalid Role')

    return render(request, 'register form/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')



def insurance_create(request):
    insurance = Insurance.objects.all()

    form = InsuranceForm()
    if request.method == 'POST':
            form = InsuranceForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('insurance_list') 

    return render(request, 'admin temp/insurance_form.html', {'form': form,'insurance': insurance})



# View to list all insurance information
def insurance_list(request):
    insurance = Insurance.objects.all()

    paginator = Paginator(insurance, 5)

    page_number = request.GET.get('page')

    try:
        page = paginator.get_page(page_number)
    except EmptyPage:
        page = paginator.page(page_number.num_pages)

    return render(request,'admin temp/insurance_list.html',{'page':page})


# View to edit insurance information
def insurance_edit (request, ins_id):
    insurance = get_object_or_404(Insurance, id=ins_id)
    if request.method == 'POST':
        form = InsuranceForm(request.POST, instance=insurance)
        if form.is_valid():
            form.save()
            return redirect('insurance_list')
    else:
        form = InsuranceForm(instance=insurance)
    return render(request, 'admin temp/insurance_form.html', {'form': form})


def insurance_delete(request,ins_id):
        insurance = Insurance.objects.get(id=ins_id)

        if request.method == 'POST':
            insurance.delete()

            return redirect('insurance_list')

        return render(request, 'admin temp/insurance_delete.html', {'insurance': insurance})


def insurance_details(request,ins_id):

    insurance = Insurance.objects.get(id=ins_id)

    return render(request, 'admin temp/insurance_detail.html', {'insurance': insurance})


def patient_insurance_list(request):
    insurance = Insurance.objects.all()
    paginator = Paginator(insurance, 8) 

    page_number = request.GET.get('page')
    insurance = paginator.get_page(page_number)


    return render(request, 'patient temp/patient_insurance_list.html',{'insurance': insurance})


def insurancelist(request, ins_id):
    insurance = AdminDoctorTable.objects.get(id=ins_id)
    return render(request, 'patient temp/patient_insurance_list.html',{'insurance': insurance})







# stripe.api_key = settings.STRIPE_SECRET_KEY

# def insurance_Details(request, ins_id):
#     # Get the selected insurance plan based on the provided id
#     insurance = Insurance.objects.get(id=ins_id)

#     if request.method == 'POST':
#         form = BillingDetailForm(request.POST)
#         if form.is_valid():
#             # Save the Billing Details
#             billing_details = form.save()

#             # Create an OrderDetail for this insurance and billing details
#             order = OrderDetail.objects.create(
#                 billing_detail=billing_details,
#                 insurance=insurance,
#                 payment_intent_id=None  # Placeholder for Stripe payment intent
#             )

#             # Create a PaymentIntent with Stripe (amount in cents)
#             try:
#                 payment_intent = stripe.PaymentIntent.create(
#                     amount=int(insurance.monthly_premium * 100),  # Convert to cents
#                     currency='inr',  # Adjust currency as needed
#                     metadata={'order_id': order.id}  # Store order id for future reference
#                 )

#                 # Save the PaymentIntent ID in the OrderDetail model
#                 order.payment_intent_id = payment_intent['id']
#                 order.save()

#                 # Return client secret to frontend
#                 # return JsonResponse({'client_secret': payment_intent['client_secret']})
#                 return redirect('purchase_success', order_id=order.id)

#             except stripe.error.StripeError as e:
#                 return JsonResponse({'error': str(e)})

#     else:
#         form = BillingDetailForm()

#     return render(request, 'patient temp/purchase_insurance.html', {'insurance': insurance, 'form': form})

def insurance_Details(request, ins_id):
    # Get the selected insurance plan based on the provided id
    insurance = get_object_or_404(Insurance, id=ins_id)

    if request.method == 'POST':
        form = BillingDetailForm(request.POST)
        if form.is_valid():
            # Save the Billing Details
            billing_detail = form.save(commit=False)
            billing_detail.payment_method = request.POST.get('payment_method')

            # Save additional payment details conditionally
            if billing_detail.payment_method == 'Debit Card':
                billing_detail.card_number = request.POST.get('card_number')
                billing_detail.card_expiry = request.POST.get('card_expiry')
                billing_detail.card_cvv = request.POST.get('card_cvv')
            elif billing_detail.payment_method == 'UPI':    
                billing_detail.upi_id = request.POST.get('upi_id')  # Mark payment as completed
            
            billing_detail.save()

            # Create an OrderDetail for this insurance and billing details
            order = OrderDetail.objects.create(
                billing_detail=billing_detail,
                insurance=insurance,
                payment_intent_id=None  # No payment intent since no gateway is used
            )

            # Redirect to the success page with the order ID
            return redirect('purchase_success', order_id=order.id)

    else:
        form = BillingDetailForm()

    return render(request, 'patient temp/purchase_insurance.html', {        
        'insurance': insurance,
        'form': form,
        'insurance_price': insurance.price
    })


def purchase_success(request, order_id):
    order = get_object_or_404(OrderDetail, id=order_id)
    return render(request, 'patient temp/purchase_success.html', {'order': order})



# def purchase_success(request, order_id):
#     try:
#         order = OrderDetail.objects.get(id=order_id)
#         # Retrieve PaymentIntent
#         payment_intent = stripe.PaymentIntent.retrieve(order.payment_intent_id)

#         if payment_intent['status'] == 'succeeded':
#             order.billing_detail.payment_status = 'Paid'
#             order.billing_detail.save()
#             return render(request, 'purchase_success.html', {'order': order})
#         else:
#             return render(request, 'purchase_failed.html')

#     except OrderDetail.DoesNotExist:
#         return redirect('insurance_details', ins_id=order.insurance.id)



def orders(request):

    orders = OrderDetail.objects.all()

    paginator = Paginator(orders, 5)

    page_number = request.GET.get('page')

    try:
        page = paginator.get_page(page_number)
    except EmptyPage:
        page = paginator.page(page_number.num_pages)

    return render(request,'admin temp/orders.html',{'page':page})


def orderDetails(request,ord_id):

    orders = OrderDetail.objects.get(id=ord_id)

    return render(request, 'admin temp/order_detail.html', {'orders': orders})




def billing(request):

    billing = BillingDetail.objects.all()

    paginator = Paginator(billing, 5)

    page_number = request.GET.get('page')

    try:
        page = paginator.get_page(page_number)
    except EmptyPage:
        page = paginator.page(page_number.num_pages)

    return render(request,'admin temp/billing.html',{'page':page})



def billingDetails(request,bil_id):

    billing = BillingDetail.objects.get(id=bil_id)

    return render(request, 'admin temp/billing_detail.html', {'billing': billing})



def paymentstatus(request,pay_id):

    billing = BillingDetail.objects.get(id=pay_id)

    if request.method=='POST':
        form = PaymentStatusForm(request.POST,instance=billing)

        if form.is_valid():
            form.save()
            return redirect('billing')
    else:
        form=PaymentStatusForm(instance=billing)
    return render(request,'admin temp/payment_status.html',{'form':form})


def billing_delete(request,bil_id):
        billing = BillingDetail.objects.get(id=bil_id)

        if request.method == 'POST':
            billing.delete()

            return redirect('billing')

        return render(request, 'admin temp/billing_delete.html', {'billing': billing})


def billingpatient(request):
    billing = BillingDetail.objects.all()

    paginator = Paginator(billing, 5)

    page_number = request.GET.get('page')

    try:
        page = paginator.get_page(page_number)
    except EmptyPage:
        page = paginator.page(page_number.num_pages)

    return render(request,'patient temp/bill_detail.html',{'page':page})


def billstatus(request,bill_id):

    bill = BillingDetail.objects.get(id=bill_id)

    if request.method=='POST':
        form = PaymentStatusForm(request.POST,instance=bill)

        if form.is_valid():
            form.save()
            return redirect('billingpatient')
    else:
        form=PaymentStatusForm(instance=bill)
    return render(request,'patient temp/bill_status.html',{'form':form})


def billingdetails(request,bill_id):

    bill = BillingDetail.objects.get(id=bill_id)

    return render(request, 'patient temp/bill_info.html', {'bill': bill})




