from django.urls import path
from .views import *
urlpatterns = [
    # company endpoints
    path('company/list/',CompanyListAPI.as_view()),
    path('company/create/',CompanyCreateAPI.as_view()),
    path('company/retrieve-destroy/<int:pk>/',CompanyRetrieveDestroyAPI.as_view()),
    path('company/update/<int:pk>',CompanyUpdateAPI.as_view()),

    # department end points 
    path('department/list/',DepartmentListAPI.as_view()),
    path('department/create/',DepartmentCreateAPI.as_view()),
    path('department/retrieve-destroy/<int:pk>/',DepartmentRetrieveDestroyAPI.as_view()),
    path('department/update/<int:pk>/',DepartmentUpdateAPI.as_view()),

]
