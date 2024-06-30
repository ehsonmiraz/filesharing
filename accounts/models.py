from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.
class User(AbstractUser):
    is_ops_user = models.BooleanField(default=False)
    is_client_user = models.BooleanField(default=False)
