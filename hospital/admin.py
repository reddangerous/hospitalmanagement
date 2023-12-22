from django.contrib import admin
from .models import Doctor,Patient,Appointment,PatientDischargeDetails,Supplier,Drug, Prescription
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Doctor, DoctorAdmin)

class PatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patient, PatientAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Appointment, AppointmentAdmin)

class PatientDischargeDetailsAdmin(admin.ModelAdmin):
    pass
admin.site.register(PatientDischargeDetails, PatientDischargeDetailsAdmin)

class DrugAdmin(admin.ModelAdmin):
    pass

admin.site.register(Drug, DrugAdmin)

class SupplierAdmin(admin.ModelAdmin):
    pass
admin.site.register(Supplier, SupplierAdmin)

class PrescriptionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Prescription, PrescriptionAdmin)

