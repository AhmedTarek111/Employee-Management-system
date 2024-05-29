from django.shortcuts import render
from rest_framework.generics import  ListAPIView ,CreateAPIView,RetrieveDestroyAPIView,UpdateAPIView
from .serializers import EmployeeListRetrieveDestroySerializer,EmployeeCreateUpdateSerializer
from .models import Employee

class EmployeeListAPI(ListAPIView):
    serializer_class = EmployeeListRetrieveDestroySerializer
    queryset = Employee.objects.all()
    
    
class EmployeeCreateAPI(CreateAPIView):
    serializer_class = EmployeeCreateUpdateSerializer
    queryset = Employee.objects.all()
    
    
class EmployeeUpdateAPI(UpdateAPIView):
    serializer_class = EmployeeCreateUpdateSerializer
    queryset = Employee.objects.all()
    
class EmployeeRetrieveDestroyAPI(RetrieveDestroyAPIView):
    serializer_class  = EmployeeListRetrieveDestroySerializer
    queryset = Employee.objects.all()