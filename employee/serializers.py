from rest_framework import serializers 
from .models import Employee
from company.serializers import DepartmentSerializer
class EmployeeSerializer(serializers.ModelSerializer):
    department =DepartmentSerializer(source='department_employee')
    company = serializers.StringRelatedField()
    class Meta:
        model = Employee
        fields = '__all__'
        read_only_fields = ('status','hired_on','days_employed')
        