# Generated by Django 5.0 on 2024-02-28 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0037_remove_patientdischargedetails_prescriptions_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientdischargedetails',
            name='prescriptions',
        ),
    ]
