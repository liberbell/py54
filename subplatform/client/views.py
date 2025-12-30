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
        return redirect("client-dashboard")
    
    current_subscription_plan = subDetails.subscription_plan

    if current_subscription_plan == "Standard":
        articles = Article.objects.all().filter(is_premium=False)