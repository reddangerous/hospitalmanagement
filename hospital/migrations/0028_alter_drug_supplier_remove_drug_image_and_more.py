# Generated by Django 5.0 on 2024-01-30 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0027_medication_drug_alter_medication_price_per_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='supplier',
            field=models.CharField(default='David Suppliers', max_length=255),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='drug',
            name='image',
        ),
        migrations.DeleteModel(
            name='Supplier',
        ),
    ]
