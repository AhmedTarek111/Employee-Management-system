from django.shortcuts import render
from rest_framework.generics import  ListAPIView ,CreateAPIView,RetrieveDestroyAPIView,UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmployeeListRetrieveDestroySerializer,EmployeeCreateUpdateSerializer
from .models import Employee 
from company.models import Company
from rest_framework.permissions import AllowAny,IsAuthenticated

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
    permission_classes=[AllowAny]
    
    
# to list employees related to spcific company
class EmployeesRelatedToCompanyAPI(APIView):
    serializer_class = EmployeeListRetrieveDestroySerializer
    permission_classes=[AllowAny]
    def get(self,request,companyId):
        company = Company.objects.get(id=companyId)
        employees = Employee.objects.filter(company= company)
        data= EmployeeListRetrieveDestroySerializer(employees,many=True).data
        return Response(data,status=status.HTTP_200_OK)