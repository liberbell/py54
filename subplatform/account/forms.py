from django.contrib.auth.forms import UserCreationForm
from . models import CustomUser

class CreateUserForm(UserCreationForm):

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'