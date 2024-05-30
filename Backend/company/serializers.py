from rest_framework import serializers
from .models import Company, Department

class CompanyListRetrieveDestroySerializer(serializers.ModelSerializer):
        class Meta:
            model = Company
            fields = '__all__'

class CompanyCreateUpdateSerializer(serializers.ModelSerializer):
      class Meta:
            model = Company
            fields = ('name',)


class DepartmentListRetrieveDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        
class DepartmentCreateUpdateSerializer(serializers.ModelSerializer):
      class Meta:
            model = Department
            fields = ('company','name')
