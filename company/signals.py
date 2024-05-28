from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Department, Company
from employee.models import Employee

@receiver([post_save, post_delete], sender=Employee)
def update_employee_count(sender, instance, **kwargs):
    company = instance.company
    if company:
        company.number_of_employees = company.company_employee.count()
        company.save()

@receiver([post_save, post_delete], sender=Department)
def update_all_departments_count(sender, instance, **kwargs):
    company = instance.company
    if company:
        company.number_of_departments = company.department_company.count()
        company.save()

@receiver([post_save, post_delete], sender=Employee)
def update_employee_of_department_count(sender, instance, **kwargs):
    department = instance.department
    if department:
        department.number_of_employees = department.department_employee.count()
        department.save()
