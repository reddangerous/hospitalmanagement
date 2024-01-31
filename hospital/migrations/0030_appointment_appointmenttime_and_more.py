# Generated by Django 5.0 on 2024-01-30 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0029_alter_appointment_appointmentdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='appointmentTime',
            field=models.TimeField(default='08:00:00'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointmentDate',
            field=models.DateField(),
        ),
    ]