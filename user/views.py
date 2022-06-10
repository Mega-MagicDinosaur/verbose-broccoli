from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
from django.views.decorators.csrf import csrf_protect

from user.forms import *


def login_page_redirect(request):
    return redirect('login_page')


@csrf_protect
def signup_page(request):
    exceptions = {'taken_username_exc': False}
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            if not User.objects.filter(username=email):  # change to get
                user = User.objects.create_user(username=email, password=password)  # EMAIL IS USED AS A USERNAME!!!
                user.save()
                return redirect('login_page')
            else:
                exceptions['taken_username_exc'] = True
    else:
        form = SignupForm()
    context = {'form': form, 'exceptions': exceptions}
    return render(request, 'user/signup.html', context)


@csrf_protect
def login_page(request):
    exceptions = {'auth_failed_exc': False}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user=user)
                return redirect('home_page', user.id)
            else:
                exceptions['auth_failed_exc'] = True
    else:
        form = LoginForm()
    context = {'form': form, 'exceptions': exceptions}
    return render(request, 'user/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('index_page')
