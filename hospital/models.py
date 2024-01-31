from django.db import models
from django.contrib.auth.models import User



departments=[('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]
class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    department= models.CharField(max_length=50,choices=departments,default='Cardiologist')
    status=models.BooleanField(default=False)
    availableForAppointment = models.BooleanField(default=True)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)



class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    symptoms = models.CharField(max_length=100,null=False)
    assignedDoctorId = models.PositiveIntegerField(null=True)
    admitDate=models.DateField(auto_now=True)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name+" ("+self.symptoms+")"


class Appointment(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    appointmentDate=models.DateField()
    appointmentTime = models.TimeField()
    description=models.TextField(max_length=500)
    status=models.BooleanField(default=False)



class PatientDischargeDetails(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40)
    assignedDoctorName=models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    symptoms = models.CharField(max_length=100,null=True)

    admitDate=models.DateField(null=False)
    releaseDate=models.DateField(null=False)
    daySpent=models.PositiveIntegerField(null=False)

    roomCharge=models.PositiveIntegerField(null=False)
    medicineCost=models.PositiveIntegerField(null=False)
    doctorFee=models.PositiveIntegerField(null=False)
    OtherCharge=models.PositiveIntegerField(null=False)
    total=models.PositiveIntegerField(null=False)


class Drug(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    date_received = models.DateField()
    supplier = models.CharField(max_length=255)
    description = models.TextField()
    def total_price(self):
        return self.quantity * self.price_per_unit

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_prescribed = models.DateTimeField(auto_now_add=True)
    #defining a way to fetch patients name and adding it here
    @property
    def patient_name(self):
        return self.patient.get_name
  



from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Activity(models.Model):
    ACTION_CHOICES = [
        ('ADD', 'Add'),
        ('DELETE', 'Delete'),
        ('UPDATE', 'Update'),
        ('RESTOCK', 'Restock'),
        ('GENERATE_REPORT', 'Generate Report'),
        ('PRESCRIBE', 'Prescribe')
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    # Calculated fields
    quantity = models.PositiveIntegerField(null=True)
    total_value = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return f'{self.action} - {self.drug.name}'

# Signal to update Activity model when Drug model is saved
@receiver(post_save, sender='hospital.Drug')
def update_activity(sender, instance, created, **kwargs):
    if created:
        # If a new drug is added, record an 'ADD' activity
        Activity.objects.create(
            drug=instance,
            action='ADD',
            quantity=instance.quantity,
            total_value=instance.total_price(),
            
        )
    else:
        # If an existing drug is updated, record an 'UPDATE' activity
        Activity.objects.create(
            drug=instance,
            action='UPDATE',
            quantity=instance.quantity,
            total_value=instance.total_price(),
            
        )
from django.db import models

class Medication(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_dispensed = models.DateField()
    quantity_dispensed = models.PositiveIntegerField()
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    # def price_per_unit(self):
    #     return self.drug.price_per_unit if self.drug else None

    # @property
    # def prescription_amount(self):
    #     return self.price_per_unit * self.quantity_dispensed if self.price_per_unit else None

    # @property
    # def total_price(self):
    #     return self.quantity_dispensed * self.price_per_unit if self.price_per_unit else None
    
    # @property
    # def total_price_after_margin(self):
    #     return self.quantity_dispensed * self.price_per_unit * 1.2 if self.price_per_unit else None
#Developed By : sumit kumar
#facebook : fb.com/sumit.luv
#Youtube :youtube.com/lazycoders
