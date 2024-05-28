from rest_framework import serializers 
from .models import Employee
from company.serializers import DepartmentListRetrieveSerializer
from datetime import date

class EmployeeSerializer(serializers.ModelSerializer):
    department =DepartmentListRetrieveSerializer(source='department_employee')
    company = serializers.StringRelatedField()

    def validate_email(self, value):
        if "@" not in value:
            raise serializers.ValidationError("This is not a valid email address.")
        return value

    def validate_mobile_number(self, value):
        if len(str(value)) < 10:
            raise serializers.ValidationError("Mobile number must be at least 10 digits long.")
        return value

   
   
    class Meta:
        model = Employee
        fields = '__all__'
        read_only_fields = ('status','hired_on','days_employed')