from django.shortcuts import render, redirect
from myApp.models import URL
import random
import string
from django.views.generic.base import RedirectView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def create_short_url(request):
    if not request.user.is_authenticated:
        return redirect('login')
    shortened_url = None
    if request.method == "POST":
        original_url = request.POST.get("original_url")
        shortened_url = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        url = URL(user=request.user, original_url=original_url, shortened_url=shortened_url)
        url.save()
    return render(request, 'create_url.html', {'shortened_url': shortened_url})


def redirect_url(request, shortenedd):
    url = URL.objects.get(shortened_url=shortenedd)
    return RedirectView.as_view(url=url.original_url, permanent=True)(request)

def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(username,password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    else:
        return render(request, 'login.html')

def logoutuser(request):
    if not request.user.is_authenticated:
        return redirect('login')
    logout(request)
    return render(request, "logout.html")   

def signupuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error_message': 'Username already exists'})
        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error_message': 'Email already exists'})
        user = User.objects.create_user(username, email, password)
        user.first_name = fname
        user.last_name = lname
        user.save()
        print(username,password,email)
        return redirect('login')
    return render(request, "signup.html")

@login_required(login_url='/login')
def dashboard(request):
    urls = URL.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'urls': urls})


