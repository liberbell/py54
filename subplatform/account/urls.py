from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name=""),
    path('register', views.register, name="register"),
    path('my-login', views.my_login, name="my-login"),
    path('user-logout', views.user_logout, name="user-logout"),
    path('reset_password', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_passwor_sent', auth_views.PasswordResetDoneView.as_view(), name="reset_password_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]