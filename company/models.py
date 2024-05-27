from django.db import models

class Company(models.Model):
    name = models.CharField(verbose_name='Company Name',max_length=100)
    number_of_departments = models.IntegerField(verbose_name='Number of departments')
    number_of_employees = models.IntegerField(verbose_name='Number of Employees')
    
    
class Department(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='department_company')
    name = models.CharField(verbose_name='Department Name',max_length=100,)
    number_of_employees = models.IntegerField(verbose_name='number_of_employees')