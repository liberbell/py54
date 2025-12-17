from django.urls import path
from . import views

urlpatterns = [
    path('client-dashboard', views.writer_dashboard, name="client-dashboard"),
]
