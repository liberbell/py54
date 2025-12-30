from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from writer.models import Article
from . models import Subscription

# Create your views here.
@login_required(login_url="my-login")
def client_dashboard(request):

    return render(request, "client/client-dashboard.html")

@login_required(login_url="my-login")
def browse_articles(request):

    try:
        subDetails = Subscription.objects.get(user=request.user, is_active=True)
    except: