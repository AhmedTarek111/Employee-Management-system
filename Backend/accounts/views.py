from rest_framework import  status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,UpdateAPIView
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework.permissions import IsAuthenticated,AllowAny
from .serializer import UserCreateSerializer, UserUpdateSerializer
from rest_framework_simplejwt.tokens import AccessToken
from company.models import Department,Company
from employee.models import Employee
from django.http import JsonResponse

class UserRegisteringApi(APIView):
    queryset = get_user_model().objects.all()  
    serializer_class = UserCreateSerializer
    permission_classes=[AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
    
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
    
class UserRetrieve(APIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user 
        if user:
            user_data = UserUpdateSerializer(user).data
            return Response(user_data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)


class UpdateUser(UpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated]
    queryset = get_user_model().objects.all()
    def put(self, request, *args, **kwargs):
        user_id = kwargs['pk']
        user = get_user_model().objects.get(pk=user_id)
        group_names = {
                'Admin': 'Admin',
                'Manager': 'Manager',
                'Employee': 'Employee'  
            }
        
        serializer = self.get_serializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        if 'role' in request.data:
            role = request.data['role']
            group_names = {
                'Admin': 'Admin',
                'Manager': 'Manager',
                'Employee': 'Employee'  
            }
        group = Group.objects.get(name=group_names[role])
        group.user_set.add(user)        
        serializer.save()

        return Response(serializer.data)
    
    
class HomepageView(APIView):
    permission_classes = [IsAuthenticated] 
    def get(self, request, *args, **kwargs):
        employee_count = Employee.objects.all().count()
        company_count = Company.objects.all().count()
        department_count = Department.objects.all().count()

        return Response({
            'employee': employee_count,
            'company': company_count,
            'department': department_count
        })