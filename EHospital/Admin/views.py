from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import logout
from django.http import Http404
from django.shortcuts import get_object_or_404, render,redirect
from django.core.paginator import Paginator,EmptyPage
from Admin.forms import AppointmentForm, BlogForm,ContactForm,ScheduleForm,PrescriptionForm
from Doctor.models import BlogPosting, Prescription
from .models import AdminPatientTable, LoginTable, AdminDoctorTable,ContactTable
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