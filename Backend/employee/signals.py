from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Employee

@receiver([post_save, post_delete], sender=Employee)
def update_employee_count(sender, instance, **kwargs):
    company = instance.company
    company.number_of_employees = company.company_employee.count()
    company.save()