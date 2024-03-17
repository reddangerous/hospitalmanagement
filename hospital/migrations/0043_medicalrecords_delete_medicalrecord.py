# Generated by Django 5.0 on 2024-03-12 10:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0042_medicalrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='medicalRecords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medication_name', models.CharField(max_length=100)),
                ('dosage', models.CharField(max_length=50, null=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('hospital_name', models.CharField(blank=True, max_length=100, null=True)),
                ('discharge_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical_records', to='hospital.patientdischargedetails')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical_records', to='hospital.patient')),
                ('recommendation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical_records', to='hospital.recommendation')),
            ],
        ),
        migrations.DeleteModel(
            name='MedicalRecord',
        ),
    ]