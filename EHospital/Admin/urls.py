from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home' ),
    path('about/',views.about,name='about'),
    path('feature/',views.feature,name='feature'),
    path('maincontact/',views.contact,name='maincontact'),
    path('service/',views.service,name='service'),
    path('testimonial/',views.testimonial,name='testimonial'),



    path('patientbase/',views.patientbase,name='patientbase' ),
    path('patienthome/',views.patienthome,name='patienthome' ),
    path('patientabout/',views.patientabout,name='patientabout' ),
    path('patientservice/',views.patientservice,name='patientservice' ),
    path('patientappointment/',views.patientappointment,name='patientappointment' ),
    path('patientfeature/',views.patientfeature,name='patientfeature' ),
    path('patientcontact/',views.patientcontact,name='patientcontact' ),
    path('patientdoctor/',views.patientdoctor,name='patientdoctor' ),
    path('patientdetails/<int:docid>/',views.doctorlist,name='doctorlist' ),
    path('appointmentsuccess/',views.appointmentsuccess,name='success' ),
    path('contact/',views.patientcontact,name='contact' ),
    path('patientblog/',views.patientblog,name='patientblog' ),
    path('blogdetails/<int:docid>/',views.bloglist,name='patientblogdetail' ),


    path('register/',views.Registration,name='register' ),
    path('doctorregister/',views.DoctorRegistration,name='doctorregister' ),
    path('doctorhome/',views.doctorhome,name='doctorhome' ),
    path('doctorabout/',views.doctorabout,name='doctorabout' ),
    path('doctorservice/',views.doctorservice,name='doctorservice' ),
    path('doctorcontact/',views.doctorcontact,name='doctorcontact' ),
    path('searchAppointment/',views.Search_Appointment,name='search'),

    path('doctorappointmentlist/',views.doctorListView,name='doctorappointment' ),
    path('AppointmentUpdate/<int:appoin_id>/',views.appointmentUpdate,name='appointment_update'),
    path('AppointmentDelete/<int:appoin_id>/',views.appointmentDelete,name='appointment_delete'),


    path('prescription/<int:appoin_id>/',views.prescription,name='prescription'),
    path('prescriptionlist/',views.prescriptionlist,name='prescriptionlist'), 
    path('Prescriptiondetail/<int:pre_id>/',views.Prescriptiondetail,name='prescription_detail'),   
    path('PrescriptionUpdate/<int:pre_id>/',views.prescriptionUpdate,name='prescription_update'),
    path('prescriptionDelete/<int:pre_id>/',views.prescriptionDelete,name='prescription_delete'),


    path('blog/',views.blog,name='blog'),
    path('createblog/',views.createBlog,name='create_blog'),
    path('Blogdetail/<int:blog_id>/',views.Blogdetail,name='blog_detail'),   
    path('blog_delete/<int:blog_id>/',views.blogdelete,name='blog_Delete'),
    path('BlogUpdate/<int:blog_id>/',views.blogUpdate,name='blog_update'),


    path('admindashboard/',views.admin_view,name='admin_view'),
    path('detail/<int:user_id>/',views.detailsView,name='details'),
    path('update/<int:user_id>/',views.update_user,name='update'),
    path('userdelete/<int:user_id>/',views.userdelete,name='userdelete'),


    path('doctor/',views.doctor_view,name='doctor_view'),
    path('doctordetail/<int:user_id>/',views.doctorDetails,name='doctordetails'),
    path('doctorupdate/<int:user_id>/',views.update_doctor,name='doctorupdate'),
    path('doctordelete/<int:user_id>/',views.doctordelete,name='doctordelete'),


    path('adminblog/',views.adminblog,name='adminblog'),
    path('admincreateblog/',views.admincreateBlog,name='createblog'),
    path('adminBlogdetail/<int:blog_id>/',views.adminBlogdetail,name='blogdetail'),   
    path('adminblog_delete/<int:blog_id>/',views.adminblogdelete,name='blogDelete'),
    path('adminBlogUpdate/<int:blog_id>/',views.adminblogUpdate,name='blogupdate'),


    path('adminprescriptionlist/',views.adminprescriptionlist,name='prescription_list'), 
    path('adminPrescriptiondetail/<int:pre_id>/',views.adminPrescriptiondetail,name='prescriptiondetail'), 
    path('adminPrescriptionUpdate/<int:pre_id>/',views.adminprescriptionUpdate,name='prescriptionupdate'),
    path('adminprescriptionDelete/<int:pre_id>/',views.adminprescriptionDelete,name='prescriptiondelete'),
 

    path('adminappointmentlist/',views.appointmentView,name='adminappointment' ),
    path('adminAppointmentUpdate/<int:appoin_id>/',views.adminappointmentUpdate,name='appointmentupdate'),
    path('adminAppointmentDelete/<int:appoin_id>/',views.adminappointmentDelete,name='appointmentdelete'),


    path('insurance/create/', views.insurance_create, name='insurance_create'),
    path('insurance/list/', views.insurance_list, name='insurance_list'),
    path('insurancedetail/<int:ins_id>/',views.insurance_details,name='insurance_detail'),
    path('insurance/edit/<int:ins_id>/', views.insurance_edit, name='insurance_edit'),
    path('insurancedelete/<int:ins_id>/',views.insurance_delete,name='insurance_delete'),

    path('patientinsurance/',views.patient_insurance_list,name='patient_insurance' ),
    path('purchase/<int:ins_id>/', views.insurance_Details, name='purchase_insurance'),
    path('purchase/success/<int:order_id>/', views.purchase_success, name='purchase_success'),


    path('orders/',views.orders,name='orders'), 
    path('orderdetail/<int:ord_id>/',views.orderDetails,name='orderdetail'),   

    path('billing/',views.billing,name='billing'), 
    path('billingdetail/<int:bil_id>/',views.billingDetails,name='billingdetail'),   
    path('billingstatus/<int:pay_id>/',views.paymentstatus,name='paymentstatus'),
    path('billingdelete/<int:bil_id>/',views.billing_delete,name='billingdelete'),   

    path('billingpatient/',views.billingpatient,name='billingpatient'), 
    path('billstatus/<int:bill_id>/',views.billstatus,name='billstatus'),
    path('billingdetails/<int:bill_id>/',views.billingdetails,name='billingDetails'),   



    path('login/',views.Login,name='login'),
    path('logout/',views.logout_view,name='logout'),


]