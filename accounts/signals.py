from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token  # For DRFT
from .models import CustomUser

@receiver(post_save, sender=CustomUser)
def create_token(sender, instance, created, **kwargs):
    if created:
        token,created= Token.objects.get_or_create(user=instance)