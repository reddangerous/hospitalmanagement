# Generated by Django 3.0.5 on 2023-12-27 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0023_activity'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='quantity',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='total_value',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
