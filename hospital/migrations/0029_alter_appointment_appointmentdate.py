# Generated by Django 5.0 on 2024-01-30 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0028_alter_drug_supplier_remove_drug_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointmentDate',
            field=models.TimeField(),
        ),
    ]
