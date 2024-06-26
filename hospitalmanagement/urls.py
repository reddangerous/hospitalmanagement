"""

Developed By : sumit kumar
facebook : fb.com/sumit.luv
Youtube :youtube.com/lazycoders


"""




from django.contrib import admin
from django.urls import path
from hospital import views
from django.contrib.auth.views import LoginView,LogoutView


#-------------FOR ADMIN RELATED URLS
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name='home'),
    


    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),


    path('adminclick', views.adminclick_view),
    path('doctorclick', views.doctorclick_view),
    path('patientclick', views.patientclick_view),

    path('adminsignup', views.admin_signup_view),
    path('doctorsignup', views.doctor_signup_view,name='doctorsignup'),
    path('patientsignup', views.patient_signup_view),
    path('admissionrepsignup', views.admissionrep_signup_view, name='admissionrepsignup'),
    path('pharmacistsignup', views.pharmacist_signup_view, name='pharmasistsignup'),
    path('financerepsignup', views.financerep_signup_view, name='financerepsignup'),
    
    path('adminlogin', LoginView.as_view(template_name='hospital/adminlogin.html')),
    path('doctorlogin', LoginView.as_view(template_name='hospital/doctorlogin.html')),
    path('patientlogin', LoginView.as_view(template_name='hospital/patientlogin.html')),
    path('admissionreplogin', LoginView.as_view(template_name='hospital/admissionreplogin.html')),
    path('pharmacistlogin', LoginView.as_view(template_name='hospital/pharmacistlogin.html')),
    path('financereplogin', LoginView.as_view(template_name='hospital/financereplogin.html')),


    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),


    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
    path('admissionrep-dashboard', views.admissionrep_dashboard_view,name='admissionrep-dashboard'),
    path('pharmacist-dashboard', views.pharmacy_view,name='pharmacist-dashboard'),
    path('financerep-dashboard', views.financial_management_dashboard,name='financerep-dashboard'),

    path('admin-doctor', views.admin_doctor_view,name='admin-doctor'),
    path('admin-view-doctor', views.admin_view_doctor_view,name='admin-view-doctor'),
    path('delete-doctor-from-hospital/<int:pk>', views.delete_doctor_from_hospital_view,name='delete-doctor-from-hospital'),
    path('update-doctor/<int:pk>', views.update_doctor_view,name='update-doctor'),
    path('admin-add-doctor', views.admin_add_doctor_view,name='admin-add-doctor'),
    path('admin-approve-doctor', views.admin_approve_doctor_view,name='admin-approve-doctor'),
    path('approve-doctor/<int:pk>', views.approve_doctor_view,name='approve-doctor'),
    path('reject-doctor/<int:pk>', views.reject_doctor_view,name='reject-doctor'),
    path('admin-view-doctor-specialisation',views.admin_view_doctor_specialisation_view,name='admin-view-doctor-specialisation'),


    path('admin-patient', views.admin_patient_view,name='admin-patient'),
    path('admin-view-patient', views.admin_view_patient_view,name='admin-view-patient'),
    path('delete-patient-from-hospital/<int:pk>', views.delete_patient_from_hospital_view,name='delete-patient-from-hospital'),
    path('update-patient/<int:pk>', views.update_patient_view,name='update-patient'),
    path('admin-add-patient', views.admin_add_patient_view,name='admin-add-patient'),
    path('admin-approve-patient', views.admin_approve_patient_view,name='admin-approve-patient'),
    path('approve-patient/<int:pk>', views.approve_patient_view,name='approve-patient'),
    path('reject-patient/<int:pk>', views.reject_patient_view,name='reject-patient'),
    path('admin-discharge-patient', views.admin_discharge_patient_view,name='admin-discharge-patient'),
    path('discharge-patient/<int:pk>', views.discharge_patient_view,name='discharge-patient'),
    path('download-pdf/<int:pk>', views.download_pdf_view,name='download-pdf'),

    path('add_department/', views.add_department, name='add_department'),
    path('admin-appointment', views.admin_appointment_view,name='admin-appointment'),
    path('admin-view-appointment', views.admin_view_appointment_view,name='admin-view-appointment'),
    path('admin-add-appointment', views.admin_add_appointment_view,name='admin-add-appointment'),
    path('admin-approve-appointment', views.admin_approve_appointment_view,name='admin-approve-appointment'),
    path('approve-appointment/<int:pk>', views.approve_appointment_view,name='approve-appointment'),
    path('reject-appointment/<int:pk>', views.reject_appointment_view,name='reject-appointment'),
]

#Admission rep urls
urlpatterns +=[
    path('admission-doctor', views.admission_doctor_view,name='admin-doctor'),
    path('admission-view-doctor', views.admission_view_doctor_view,name='admission-view-doctor'),
    path('delete-doctor-from-hospital/<int:pk>', views.delete_doctor_from_hospital_view,name='delete-doctor-from-hospital'),
    path('update-doctor/<int:pk>', views.update_doctor_view,name='update-doctor'),
    path('admission-add-doctor', views.admission_add_doctor_view,name='admission-add-doctor'),
    path('admission-approve-doctor', views.admission_approve_doctor_view,name='admission-approve-doctor'),
    path('approve-doctor/<int:pk>', views.approve_doctor_view,name='approve-doctor'),
    path('reject-doctor/<int:pk>', views.reject_doctor_view,name='reject-doctor'),
    path('admission-view-doctor-specialisation',views.admission_view_doctor_specialisation_view,name='admission-view-doctor-specialisation'),


    path('admission-patient', views.admission_patient_view,name='admission-patient'),
    path('admission-view-patient', views.admission_view_patient_view,name='admission-view-patient'),
    path('delete-patient-from-hospital/<int:pk>', views.delete_patient_from_hospital_view,name='delete-patient-from-hospital'),
    path('update-patient/<int:pk>', views.update_patient_view,name='update-patient'),
    path('admission-add-patient', views.admission_add_patient_view,name='admission-add-patient'),
    path('admission-approve-patient', views.admission_approve_patient_view,name='admission-approve-patient'),
    path('approve-patient/<int:pk>', views.approve_patient_view,name='approve-patient'),
    path('reject-patient/<int:pk>', views.reject_patient_view,name='reject-patient'),
    path('admission-discharge-patient', views.admission_discharge_patient_view,name='admission-discharge-patient'),
    path('discharge-patient/<int:pk>', views.discharge_patient_view,name='discharge-patient'),
    path('download-pdf/<int:pk>', views.download_pdf_view,name='download-pdf'),

    path('add_department/', views.add_department, name='add_department'),
    path('admission-appointment', views.admission_appointment_view,name='admission-appointment'),
    path('admission-view-appointment', views.admission_view_appointment_view,name='admission-view-appointment'),
    path('admission-add-appointment', views.admission_add_appointment_view,name='admission-add-appointment'),
    path('admission-approve-appointment', views.admission_approve_appointment_view,name='admission-approve-appointment'),
    path('approve-appointment/<int:pk>', views.approve_appointment_view,name='approve-appointment'),
    path('reject-appointment/<int:pk>', views.reject_appointment_view,name='reject-appointment'),
]

#---------FOR DOCTOR RELATED URLS-------------------------------------
urlpatterns +=[
    path('doctor-dashboard', views.doctor_dashboard_view,name='doctor-dashboard'),
    path('search', views.search_view,name='search'),

    path('doctor-patient', views.doctor_patient_view,name='doctor-patient'),
    path('doctor-view-patient', views.doctor_view_patient_view,name='doctor-view-patient'),
    path('doctor-view-discharge-patient',views.doctor_view_discharge_patient_view,name='doctor-view-discharge-patient'),

    path('doctor-appointment', views.doctor_appointment_view,name='doctor-appointment'),
    path('doctor-view-appointment', views.doctor_view_appointment_view,name='doctor-view-appointment'),
    path('doctor-delete-appointment',views.doctor_delete_appointment_view,name='doctor-delete-appointment'),
    path('delete-appointment/<int:pk>', views.delete_appointment_view,name='delete-appointment'),
    path('create_recommendation/<int:patient_id>/', views.create_recommendation, name='create_recommendation'),
    path('view_recommendations/<int:patient_id>/', views.view_recommendations, name='view_recommendations'),
    path('patient_view_recommendations/<int:patient_id>/', views.patient_view_recommendations, name='patient_view_recommendations'),
]   




#---------FOR PATIENT RELATED URLS-------------------------------------
urlpatterns +=[

    path('patient-dashboard', views.patient_dashboard_view,name='patient-dashboard'),
    path('patient-appointment', views.patient_appointment_view,name='patient-appointment'),
    path('patient-book-appointment', views.patient_book_appointment_view,name='patient-book-appointment'),
    path('patient-view-appointment', views.patient_view_appointment_view,name='patient-view-appointment'),
    path('patient-view-doctor', views.patient_view_doctor_view,name='patient-view-doctor'),
    path('searchdoctor', views.search_doctor_view,name='searchdoctor'),
    path('patient-discharge', views.patient_discharge_view,name='patient-discharge'),

]

#---------FOR INVENTORY RELATED URLS-------------------------------------
urlpatterns += [
    path('inventory/', views.inventory, name='inventory'),
    path('add_inventory/', views.add_inventory, name='add_inventory'),
    path('doctor_drugs/', views.doctor_view_drugs, name='doctor_view_drugs'),
    path('drug/<int:drug_id>/', views.drug_details, name='drug_details'),
    path('drug/<int:drug_id>/edit/', views.edit_drug, name='edit_drug'),
    path('drug/<int:drug_id>/delete/', views.delete_drug, name='delete_drug'),
    path('drug/<int:drug_id>/prescribe/', views.prescribe_drug, name='prescribe_drug'),
    path('drug/<int:drug_id>/doctor_prescribe_drug/', views.doctor_prescribe_drug, name='doctor_prescribe_drug'),
    path('drug/<int:drug_id>/restock/', views.restock_drug, name='restock_drug'),
    path('drug/<int:drug_id>/generate_report/', views.generate_report, name='generate_report'),
    path('fetch_drug_details/', views.fetch_drug_details, name='fetch_drug_details'),
    path('download_report/<int:drug_id>/', views.download_report, name='download_report'),
    path('inventory-dashboard/', views.inventory_dashboard, name='inventory_dashboard'),
    path('pharmacy-dashboard/', views.pharmacy_dashboard, name='pharmacy_dashboard'),
    path('reports-home/', views.reports_home, name='reports_home'),
    path('download-pdf/<int:drug_id>/', views.download_pdf, name='download_pdf'),
    path('download-excel/<int:drug_id>/', views.download_excel, name='download_excel'),
    path('search/', views.search_drugs, name='search_drugs'),
    path('delete_drug/<int:drug_id>/', views.delete_drug, name='delete_drug'),
    path('drug/<int:drug_id>/edit/', views.edit_drug, name='edit_drug'),
    path('pharmacy/', views.pharmacy_view, name='pharmacy'),
    path('prescribed-medications/', views.prescribed_medications, name='prescribed_medications'),
    path('dispense_medication/<int:patient_id>/', views.dispense_medication, name='dispense_medication'),
    path('get_prescription_data/', views.get_prescription_data, name='get_prescription_data'),
    path('select-patient/', views.select_patient, name='select_patient'),
    path('prescription-management/', views.prescription_management, name='prescription_management'),
    path('dispensed-medications/', views.dispensed_medications, name='dispensed_medications'),

    #Finance'''
    path('finance/', views.financial_management_dashboard, name='finance'),
    path('sales/', views.sales, name='sales'),
    path('expenses/', views.expenses, name='expenses'),
    path('financial-reports/', views.financial_report, name='financial_reports'),
    path('add_medical_record/<int:patient_id>/', views.add_medical_record, name='add_medical_record'),
    path('view_medical_records/<int:patient_id>/', views.view_medical_records, name='view_medical_records'),
    path('patient_view_medical_records/<int:patient_id>/', views.patient_view_medical_records, name='patient_view_medical_records'),
]
#Developed By : sumit kumar
#facebook : fb.com/sumit.luv
#Youtube :youtube.com/lazycoders
