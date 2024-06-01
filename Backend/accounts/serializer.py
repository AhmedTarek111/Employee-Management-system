from rest_framework import serializers
from .models import CustomUser
ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Manager', 'Manager'),
        ('Employee', 'Employee'),
    )

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields= ('username','email','password','role')
        
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields= ('username','email','password','role','id')