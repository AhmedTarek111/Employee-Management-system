from rest_framework import  status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from .serializer import UserSerializer

class UserRegisteringApi(CreateAPIView):
    queryset = get_user_model().objects.all()  
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        validated_data = serializer.validated_data

        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role = validated_data['role']
        )

        if 'role' in request.data:
            role = request.data['role']
            group_names = {
                'Admin': 'Admin',
                'Manager': 'Manager',
                'Employee': 'Employee'  
            }
            if role == 'Admin':
                user = get_user_model().objects.get(username=validated_data['username'])
                user.is_active =True
                user.is_staff = True
                user.is_superuser = True
                user.save()
          
            elif role == 'Manager':
                user = get_user_model().objects.get(username=validated_data['username'])
                user.is_active =True
                user.is_staff = True
                user.save()
          
            elif role == 'Employee':
                user = get_user_model().objects.get(username=validated_data['username'])
                user.is_active =True
                user.save()
                
          

            if role in group_names:
                group = Group.objects.get(name=group_names[role])
                group.user_set.add(user)
            else:
                return Response({'error': 'Invalid role provided.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
