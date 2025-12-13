from django.shortcuts import render
from . forms import CreateUserForm

# Create your views here.
def home(request):
    
    return render(request, "account/index.html")

def register(request):

    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
    
    return render(request, "account/register.html")

def my_login(request):
    
    return render(request, "account/my-login.html")