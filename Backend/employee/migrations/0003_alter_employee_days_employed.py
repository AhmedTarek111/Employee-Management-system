# Generated by Django 5.0.6 on 2024-05-27 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_employee_status_alter_employee_mobile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='days_employed',
            field=models.DateField(blank=True, null=True, verbose_name='Days Empolyed'),
        ),
    ]
