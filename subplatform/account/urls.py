from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name=""),
    path('register', views.register, name="register"),
    path('my-login', views.my_login, name="my-login"),
    path('user-logout', views.user_logout, name="user-logout"),
    path('reset_password', auth_views.PasswordResetView(), name="reset_password"),
]