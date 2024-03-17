from django.contrib import admin
from .models import Doctor,Patient,Appointment,PatientDischargeDetails,Drug, Prescription, Activity, Medication, Expense, Recommendation, medicalRecords
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


class PrescriptionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Prescription, PrescriptionAdmin)

class ActivityAdmin(admin.ModelAdmin):
    pass
admin.site.register(Activity, ActivityAdmin)

class MedicationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Medication, MedicationAdmin)

class ExpenseAdmin(admin.ModelAdmin):
    pass
admin.site.register(Expense, ExpenseAdmin)

class RecommendationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Recommendation, RecommendationAdmin)

class medicalRecordsAdmin(admin.ModelAdmin):
    pass
admin.site.register(medicalRecords, medicalRecordsAdmin)