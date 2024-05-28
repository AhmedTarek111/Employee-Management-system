from django.db import models
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from employee.models import Employee

class Company(models.Model):
    name = models.CharField(verbose_name='Company Name',max_length=100)
    number_of_departments = models.IntegerField(verbose_name='Number of departments')
    number_of_employees = models.IntegerField(verbose_name='Number of Employees')
    
class Department(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='department_company')
    name = models.CharField(verbose_name='Department Name',max_length=100,)
    number_of_employees = models.IntegerField(verbose_name='Number of Employees')
    
@receiver(post_save, sender=Employee)
@receiver(post_delete, sender=Employee)
def update_employee_count(sender, instance, **kwargs):
    company = instance.company
    company.number_of_employees = Employee.objects.filter(company=company).count()
    company.save()
    
@receiver(post_save, sender=Department)
@receiver(post_delete, sender=Department)
def update_all_departments_count(sender, instance, **kwargs):
    company = instance.company
    company.number_of_departments = Department.objects.filter(company=company).count()
    company.save()


@receiver(post_save, sender=Employee)
@receiver(post_delete, sender=Employee)
def update_employee_department_count(sender, instance, **kwargs):
    department = instance.department
    department.number_of_employees = Employee.objects.filter(department=department).count()
    department.save()
    

    