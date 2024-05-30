from django.urls import path
from .views import *
urlpatterns = [
    path('list/',EmployeeListAPI.as_view()),
    path('create/',EmployeeCreateAPI.as_view()),
    path('retrieve-destroy/<int:pk>/',EmployeeRetrieveDestroyAPI.as_view()),
    path('update/<int:pk>/',EmployeeUpdateAPI.as_view()),
    path('related-employee/<int:companyId>/',EmployeesRelatedToCompanyAPI.as_view())

]

