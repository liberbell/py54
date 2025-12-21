from django.db import models

# Create your models here.
class Article(models.Model):

    title = models.CharField(max_length=150)
    content = models.TextField(max_length=1000)
    date_posted = models.DateTimeField(auto_now_add=True)