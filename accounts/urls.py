from django.urls import path
from .views import UserRegisteringApi

urlpatterns = [
     path('signup/',UserRegisteringApi.as_view(),name='signup'),
 ]
 