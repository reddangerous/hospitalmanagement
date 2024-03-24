from django import forms
from django.contrib.auth.models import User
from . import models
from .models import Department, Drug, medicalRecords, Patient, Prescription, Medication, Expense
from django.contrib.auth.models import User
# hospital/forms.py

from django import forms
from .models import Prescription, Drug

from .models import Recommendation

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['departments']

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = medicalRecords
        fields = ['medication_name', 'dosage', 'hospital_name', 'recommendation']

    def __init__(self, *args, **kwargs):
        super(MedicalRecordForm, self).__init__(*args, **kwargs)
        self.fields['recommendation'].queryset = Recommendation.objects.values_list('doctor_recommendation', flat=True)

class RecommendationForm(forms.ModelForm):
    class Meta:
        model = Recommendation
        fields = ['doctor_recommendation']

#finance management
class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'amount', 'description', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class MedicationDispenseForm(forms.ModelForm):
    prescription_quantity = forms.IntegerField(label='Prescription Quantity')
    drug_name = forms.CharField(label='Drug Name')
    drug_id = forms.IntegerField(label='Drug Id', widget=forms.HiddenInput())  # Assuming Drug is the model for drugs
    prescription_id = forms.IntegerField(label='Prescription Id', widget=forms.HiddenInput())
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.is_bound and self.data.get('patients'):
            patient_id = self.data.get('patients')
            prescription = Prescription.objects.filter(patient_id=patient_id).first()
            if prescription:
                self.fields['prescription_quantity'].initial = prescription.quantity
                self.fields['drug_name'].initial = prescription.drug.name
                self.fields['drug_id'].initial = prescription.drug.id
                self.fields['prescription_id'].initial = prescription.id

    class Meta:
        model = Medication
        fields = ['date_dispensed', 'drug_id', 'prescription_id']  # Include the drug field here
        widgets = {
            'date_dispensed': forms.DateInput(attrs={'type': 'date'}),
            'drug_id': forms.HiddenInput(),
            'prescription_id': forms.HiddenInput()
        }


class PatientSelectionForm(forms.Form):
    patients = forms.ModelChoiceField(queryset=Patient.objects.all(), empty_label="select patient to  dispense to", to_field_name="user_id")
    class Meta:
        model = Patient
        fields = ['patients']


class ReportCriteriaForm(forms.ModelForm):
    
    class Meta:
        model = Prescription
        fields = ['patient']
    patient = forms.ModelChoiceField(queryset=models.Patient.objects.all().filter(status=True),empty_label="Patient prescribed to ", to_field_name="user_id")
    start_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                                 required=False, label='From')
    
    end_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                               required=False, label='To')

class PrescriptionManagementForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['patient', 'quantity']
#for admin signup
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class PrescribeForm(forms.ModelForm):
    patients=forms.ModelChoiceField(queryset=models.Patient.objects.all().filter(status=True),empty_label="Patient prescribed to ", to_field_name="user_id")
    class Meta:
        model=models.Prescription
        fields=['quantity']

class DrugForm(forms.ModelForm):

   class Meta:
       model = Drug
       fields = ['name', 'quantity', 'price_per_unit', 'date_received', 'description', 'supplier']
       widgets = {
           'date_received': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
       }



#for student related form
class DoctorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class DoctorForm(forms.ModelForm):
    class Meta:
        model=models.Doctor
        fields=['address','mobile','department','status','profile_pic']
    def __init__(self, *args, **kwargs):
        super(DoctorForm, self).__init__(*args, **kwargs)
        # Dynamically populate the department choices
        self.fields['department'].choices = [(dept.departments, dept.departments) for dept in Department.objects.all()]



#for teacher related form
class PatientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class PatientForm(forms.ModelForm):
    #this is the extrafield for linking patient and their assigend doctor
    #this will show dropdown __str__ method doctor model is shown on html so override it
    #to_field_name this will fetch corresponding value  user_id present in Doctor model and return it
    assignedDoctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Name and Department", to_field_name="user_id")
    class Meta:
        model=models.Patient
        fields=['address','mobile','status','symptoms','profile_pic']



class AppointmentForm(forms.ModelForm):
    doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
    patientId=forms.ModelChoiceField(queryset=models.Patient.objects.all().filter(status=True),empty_label="Patient Name and Symptoms", to_field_name="user_id")
    class Meta:
        model=models.Appointment
        fields=['description','status']


class PatientAppointmentForm(forms.ModelForm):
    doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
    class Meta:
        model=models.Appointment
        fields=['description','status']
#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))



#Developed By : sumit kumar
#facebook : fb.com/sumit.luv
#Youtube :youtube.com/lazycoders
