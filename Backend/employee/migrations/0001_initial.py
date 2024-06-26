# Generated by Django 5.0.6 on 2024-05-27 20:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('mobile_number', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=100, verbose_name='Designation (Position/Title)')),
                ('hired_on', models.DateField(blank=True, null=True)),
                ('days_employed', models.DateField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_employee', to='company.company')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='department_employee', to='company.department')),
            ],
        ),
    ]
