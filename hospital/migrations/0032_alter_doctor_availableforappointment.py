# Generated by Django 5.0 on 2024-01-31 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0031_doctor_availableforappointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='availableForAppointment',
            field=models.BooleanField(default=True),
        ),
    ]
