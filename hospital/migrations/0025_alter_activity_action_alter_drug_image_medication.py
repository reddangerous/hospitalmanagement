# Generated by Django 5.0 on 2024-01-08 08:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0024_auto_20231227_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='action',
            field=models.CharField(choices=[('ADD', 'Add'), ('DELETE', 'Delete'), ('UPDATE', 'Update'), ('RESTOCK', 'Restock'), ('GENERATE_REPORT', 'Generate Report'), ('PRESCRIBE', 'Prescribe')], max_length=20),
        ),
        migrations.AlterField(
            model_name='drug',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/drugs/'),
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_dispensed', models.DateField()),
                ('quantity_dispensed', models.PositiveIntegerField()),
                ('price_per_unit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.patient')),
                ('prescription', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hospital.prescription')),
            ],
        ),
    ]
