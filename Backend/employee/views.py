from django.shortcuts import render
from rest_framework.generics import  ListAPIView ,CreateAPIView,RetrieveDestroyAPIView,UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmployeeListRetrieveDestroySerializer,EmployeeCreateSerializer,EmployeeUpdateSerializer
from .models import Employee 
from company.models import Company
from rest_framework.permissions import AllowAny,IsAuthenticated
from datetime import datetime


class EmployeeListAPI(ListAPIView):
    serializer_class = EmployeeListRetrieveDestroySerializer
    queryset = Employee.objects.all()
    permission_classes=[IsAuthenticated]
    
    
class EmployeeCreateAPI(CreateAPIView):
    serializer_class = EmployeeCreateSerializer
    queryset = Employee.objects.all()
    permission_classes = [IsAuthenticated]
    
    
class EmployeeUpdateAPI(UpdateAPIView):
    serializer_class = EmployeeUpdateSerializer
    queryset = Employee.objects.all()
    permission_classes=[IsAuthenticated]
    
    
class EmployeeRetrieveDestroyAPI(RetrieveDestroyAPIView):
    serializer_class  = EmployeeListRetrieveDestroySerializer
    queryset = Employee.objects.all()
    permission_classes=[IsAuthenticated]
    
    
# to list employees related to spcific company
class EmployeesRelatedToCompanyAPI(APIView):
    serializer_class = EmployeeListRetrieveDestroySerializer
    permission_classes=[IsAuthenticated]
    def get(self,request,companyId):
        company = Company.objects.get(id=companyId)
        employees = Employee.objects.filter(company= company)
        data= EmployeeListRetrieveDestroySerializer(employees,many=True).data
        return Response(data,status=status.HTTP_200_OK)
    
class EmployeeHiredListAPI(ListAPIView):
    serializer_class = EmployeeListRetrieveDestroySerializer
    queryset = Employee.objects.all()
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        return Employee.objects.filter(status='Hired')