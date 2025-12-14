from django.shortcuts import render
from . forms import CreateUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    
    return render(request, "account/index.html")

def register(request):

    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("User registered.")
    
    context = {"RegisterForm": form}
    return render(request, "account/register.html", context)

def my_login(request):
    
    return render(request, "account/my-login.html")