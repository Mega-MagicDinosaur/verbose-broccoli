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
            # GET ALL FIELDS
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            # CREATE NEW USER
            if not User.objects.filter(username=email):  # change to get
                user = User.objects.create_user(username=email, password=password)  # EMAIL IS USED AS A USERNAME!!!
                user.profile.name = form.cleaned_data['name']
                user.profile.surname = form.cleaned_data['surname']
                user.profile.username = form.cleaned_data['username']
                user.profile.prefix = form.cleaned_data['prefix']
                user.profile.number = form.cleaned_data['number']
                user.profile.linkedin_user = form.cleaned_data['linkedin_user']
                user.profile.company = form.cleaned_data['company']
                user.profile.department = form.cleaned_data['department']
                user.profile.job_title = form.cleaned_data['job_title']

                user.profile.type_of_code = form.cleaned_data['type_of_code']
                user.profile.code = form.cleaned_data['code']
                user.profile.address = form.cleaned_data['address']
                user.profile.turnover = form.cleaned_data['turnover']
                user.profile.employees = form.cleaned_data['employees']
                user.profile.products = form.cleaned_data['products']
                user.profile.sectors = form.cleaned_data['sectors']
                user.profile.BOM_position = form.cleaned_data['BOM_position']
                user.profile.linkedin_company = form.cleaned_data['linkedin_company']
                user.profile.email_company = form.cleaned_data['email_company']

                user.profile.save()
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
