from django.urls import path
from .views import UserRegisteringApi,UserRetrieve,UpdateUser

urlpatterns = [
     path('signup/',UserRegisteringApi.as_view(),name='signup'),
     path('retrieve/',UserRetrieve.as_view(),name='retrieve'),
     path('update/<int:pk>/',UpdateUser.as_view(),name='user-update')
 ]
 