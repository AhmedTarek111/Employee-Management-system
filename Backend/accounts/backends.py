# yourapp/backends.py

from django.contrib.auth.backends import BaseBackend
from django.conf import settings
from .models import CustomUser  
from django.db.models import Q

class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
