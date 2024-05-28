from rest_framework import serializers
from .models import Company, Department

class CompanySerializer(serializers.ModelSerializer):
        class Meta:
            model = Company
            fields = ('name',)
            
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name',)