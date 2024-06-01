from django.urls import path
from .views import UserRegisteringApi,UserRetrieveUpdate

urlpatterns = [
     path('signup/',UserRegisteringApi.as_view(),name='signup'),
     path('retrive-update/',UserRetrieveUpdate.as_view(),name='user-retrieve-update')
 ]
 