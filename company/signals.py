from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import Department
from company.models import Employee
    
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