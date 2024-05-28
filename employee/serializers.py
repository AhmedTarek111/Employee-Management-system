from rest_framework import serializers 
from .models import Employee
from company.serializers import DepartmentListRetrieveSerializer
from datetime import date

class EmployeeSerializer(serializers.ModelSerializer):
    department =DepartmentListRetrieveSerializer(source='department_employee')
    company = serializers.StringRelatedField()

    def validate_email(self, value):
        if "@" not in value:
            raise serializers.ValidationError("this is not a valid email address")
        return value

    def validate_mobile_number(self, value):
        if len(str(value)) < 10:
            raise serializers.ValidationError("mobile number must be at least 10 digits long")
        return value

    def validate(self, data):
        if data.get('hired_on') and data['hired_on'] > date.today():
            raise serializers.ValidationError("hired date cannot be in the future")
        return data
   
    class Meta:
        model = Employee
        fields = '__all__'
        read_only_fields = ('status','hired_on','days_employed')