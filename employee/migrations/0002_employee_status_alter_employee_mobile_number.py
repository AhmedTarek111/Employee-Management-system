# Generated by Django 5.0.6 on 2024-05-27 21:48

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='status',
            field=models.CharField(choices=[('Application Received', 'Application Received'), ('Interview Scheduled', 'Interview Scheduled'), ('Hired', 'Hired'), ('Not Accepted', 'Not Accepted')], default='Application Received', max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='mobile_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]