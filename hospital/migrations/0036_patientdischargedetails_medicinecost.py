# Generated by Django 5.0 on 2024-02-28 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0035_patientdischargedetails_prescriptions'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientdischargedetails',
            name='medicineCost',
            field=models.DecimalField(decimal_places=2, default=1200, max_digits=10),
            preserve_default=False,
        ),
    ]
