from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
from django.template.defaultfilters import length
from django.contrib import messages
import re



# Create your views here.

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['password2']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'username already exists')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'email already exists')
        elif password != confirm_password:
            messages.error(request, 'password not matching')
        elif not re.fullmatch(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,}$', password):
            messages.error(request, 'password contains atleast one (0-9),(a-z),(A-Z) special characters ')
        
        else:
            user = User.objects.create_user(first_name=first_name, username=username,email=email, password=password)
            user.save()
            return redirect('signin')  
    return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'invalid credentials')
            return redirect('signin')
    return render(request, 'signin.html')


def signout(request):
    auth.logout(request)
    return redirect('/')
