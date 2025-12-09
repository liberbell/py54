from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils import timezone

# Create your models here.
class CustomUser(AbstractUser, PermissionsMixin):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=135)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(_(""), auto_now=False, auto_now_add=False)