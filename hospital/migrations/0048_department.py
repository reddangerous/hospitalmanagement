# Generated by Django 5.0 on 2024-03-23 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0047_alter_expense_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departments', models.CharField(max_length=100)),
            ],
        ),
    ]
