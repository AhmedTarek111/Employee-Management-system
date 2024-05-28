from rest_framework.generics import ListAPIView,CreateAPIView , RetrieveDestroyAPIView,UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import CompanyCreateUpdateDestroySerializer,CompanyListRetrieveSerializer,DepartmentListRetrieveSerializer,DepartmentCreateUpdateDestroySerializer  
from .models import Company,Department

# company apis
class CompanyListAPI(ListAPIView):
    serializer_class = CompanyListRetrieveSerializer
    queryset = Company.objects.all()
    # permission_classes=[IsAuthenticated]
    
class CompanyCreateAPI(CreateAPIView):
    serializer_class = CompanyCreateUpdateDestroySerializer
    queryset = Company.objects.all()
    # permission_classes=[IsAuthenticated]

class CompanyRetrieveDestroyAPI(RetrieveDestroyAPIView):
    serializer_class = CompanyCreateUpdateDestroySerializer
    queryset = Company.objects.all()
    
class CompanyUpdateAPI(UpdateAPIView):
    serializer_class = CompanyCreateUpdateDestroySerializer
    queryset = Company.objects.all()
    # permission_classes=[IsAuthenticated]
    
# department apis 
class DepartmentListAPI(ListAPIView):
    serializer_class = DepartmentListRetrieveSerializer
    queryset = Department.objects.all()
    # permission_classes=[IsAuthenticated]

class DepartmentCreateAPI(CreateAPIView):
    serializer_class = DepartmentCreateUpdateDestroySerializer
    queryset = Department.objects.all()
    # permission_classes=[IsAuthenticated]
   
class DepartmentRetrieveDestroyAPI(RetrieveDestroyAPIView):
    serializer_class = DepartmentCreateUpdateDestroySerializer
    queryset = Department.objects.all()
    # permission_classes=[IsAuthenticated]

class DepartmentUpdateAPI(UpdateAPIView):
    serializer_class = DepartmentCreateUpdateDestroySerializer
    queryset = Department.objects.all()
    # permission_classes=[IsAuthenticated]
