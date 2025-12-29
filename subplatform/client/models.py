from django.db import models
from account.models import CustomUser

class Subscription(models.Model):
    
    subscriber_name = models.CharField(max_length=100)