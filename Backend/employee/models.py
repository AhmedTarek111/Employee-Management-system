from django.db import models
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinLengthValidator
from datetime import datetime

class Employee(models.Model):
    STATUS_CHOICES = (
        ('Application Received','Application Received'),
        ('Interview Scheduled','Interview Scheduled'),
        ('Hired','Hired'),
        ('Not Accepted','Not Accepted'),
         )
    
    company = models.ForeignKey('company.Company',on_delete=models.CASCADE,related_name='company_employee')
    department = models.ForeignKey('company.Department',on_delete=models.PROTECT,related_name='department_employee')
    status = models.CharField(max_length=100, choices=STATUS_CHOICES , default = 'Application Received')
    name = models.CharField(verbose_name='Name',max_length=100)
    email = models.EmailField(verbose_name='email')
    mobile_number = PhoneNumberField(validators=[MinLengthValidator(11)])
    address = models.CharField(max_length=200)
    designation = models.CharField(verbose_name='Designation (Position/Title)',max_length=100)
    hired_on = models.DateField(null=True,blank=True)
    days_employed = models.IntegerField(verbose_name='Days Empolyed',null=True,blank=True)
    
    def save(self, *args, **kwargs):
      if self.department.company != self.company:
          raise ValueError("Please choose a department related to this company")
      
      self.mobile_number = self.mobile_number.as_international
      if self.hired_on:
            self.days_employed = (datetime.now().date() - self.hired_on).days
      super(Employee, self).save(*args, **kwargs) 
      
      
    def __str__(self):
      return self.name
