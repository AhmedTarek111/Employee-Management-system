from rest_framework import serializers
from .models import Company, Department

class CompanyListRetrieveSerializer(serializers.ModelSerializer):
        class Meta:
            model = Company
            fields = '__all__'

class CompanyCreateUpdateDestroySerializer(serializers.ModelSerializer):
      class Meta:
            model = Company
            fields = ('name',)


class DepartmentListRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        
class DepartmentCreateUpdateDestroySerializer(serializers.ModelSerializer):
      class Meta:
            model = Department
            fields = ('company','name')
