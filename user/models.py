from django.db import models
from django.conf import settings
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def createAuthToken(sender,instance,created,**kwargs):
    if created:
        Token.objects.create(user=instance)


