# Generated by Django 5.0 on 2024-02-28 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0033_remove_doctor_availableforappointment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientdischargedetails',
            name='medicineCost',
        ),
    ]
