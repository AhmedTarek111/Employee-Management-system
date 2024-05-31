from rest_framework import serializers 
from .models import Employee
from datetime import date

class EmployeeListRetrieveDestroySerializer(serializers.ModelSerializer): 
    company = serializers.StringRelatedField()
    department = serializers.StringRelatedField()
    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields =('company','department','name','email','mobile_number','address','designation')
        
class EmployeeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields =('company','department','name','email','mobile_number','address','designation','status')
        
