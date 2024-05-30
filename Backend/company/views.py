from rest_framework.generics import ListAPIView,CreateAPIView , RetrieveDestroyAPIView,UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import CompanyCreateUpdateSerializer,CompanyListRetrieveDestroySerializer,DepartmentListRetrieveDestroySerializer,DepartmentCreateUpdateSerializer  
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Company,Department
from rest_framework.permissions import AllowAny,IsAuthenticated

from rest_framework.decorators import api_view
# company apis
class CompanyListAPI(ListAPIView):
    serializer_class = CompanyListRetrieveDestroySerializer
    queryset = Company.objects.all()
    # permission_classes=[IsAuthenticated]
    
class CompanyCreateAPI(CreateAPIView):
    serializer_class = CompanyCreateUpdateSerializer
    queryset = Company.objects.all()
    # permission_classes=[IsAuthenticated]
    

class CompanyRetrieveDestroyAPI(RetrieveDestroyAPIView):
    serializer_class = CompanyListRetrieveDestroySerializer
    queryset = Company.objects.all()
    permission_classes=[AllowAny]
    
class CompanyUpdateAPI(UpdateAPIView):
    serializer_class = CompanyCreateUpdateSerializer
    queryset = Company.objects.all()
    # permission_classes=[IsAuthenticated]
    
# department apis 
class DepartmentListAPI(ListAPIView):
    serializer_class = DepartmentListRetrieveDestroySerializer
    queryset = Department.objects.all()
    # permission_classes=[IsAuthenticated]

class DepartmentCreateAPI(CreateAPIView):
    serializer_class = DepartmentCreateUpdateSerializer
    queryset = Department.objects.all()
    # permission_classes=[IsAuthenticated]
   
class DepartmentRetrieveDestroyAPI(RetrieveDestroyAPIView):
    serializer_class = DepartmentCreateUpdateSerializer
    queryset = Department.objects.all()
    # permission_classes=[IsAuthenticated]

class DepartmentUpdateAPI(UpdateAPIView):
    serializer_class = DepartmentCreateUpdateSerializer
    queryset = Department.objects.all()
    
    # permission_classes=[IsAuthenticated]
class DepartmentRelatedToCompanyAPI(ListAPIView):
    serializer_class = DepartmentListRetrieveDestroySerializer
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Department.objects.filter(company=pk)