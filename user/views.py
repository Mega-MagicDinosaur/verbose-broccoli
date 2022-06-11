from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from user.forms import *


def login_page_redirect(request):
    return redirect('login_page')


@csrf_protect
def signup_page_1(request):
    exceptions = {'taken_username_exc': False}  # use this in 2 and 3 later
    initial = {'email': request.session.get('email', None)}
    form = SignupForm1(request.POST or None, initial=initial)
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            request.session['email'] = email
            if not User.objects.filter(username=email):  # change to get eventually
                user = User.objects.create_user(username=email, password=password)  # EMAIL IS USED AS A USERNAME!!
                return redirect('signup_page_2')
            else:
                exceptions['taken_username_exc'] = True
    context = {'form': form, 'exceptions': exceptions}
    return render(request, 'user/signup.html', context)


def signup_page_2(request):
    exceptions = {}
    form = SignupForm2(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = User.objects.get(username=request.session['email'])
            user.userprofile.name = form.cleaned_data['name']
            user.userprofile.surname = form.cleaned_data['surname']
            user.userprofile.username = form.cleaned_data['username']
            user.userprofile.prefix = form.cleaned_data['prefix']
            user.userprofile.number = form.cleaned_data['number']
            user.userprofile.linkedin_user = form.cleaned_data['linkedin_user']
            user.userprofile.company = form.cleaned_data['company']
            user.userprofile.department = form.cleaned_data['department']
            user.userprofile.job_title = form.cleaned_data['job_title']
            user.userprofile.save()
            return redirect('signup_page_3')

    context = {'form': form, 'exceptions': exceptions}
    return render(request, 'user/signup.html', context)


def signup_page_3(request):
    exceptions = {}
    form = SignupForm3(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = User.objects.get(username=request.session['email'])
            user.companyprofile.type_of_code = form.cleaned_data['type_of_code']
            user.companyprofile.code = form.cleaned_data['code']
            user.companyprofile.address = form.cleaned_data['address']
            user.companyprofile.turnover = form.cleaned_data['turnover']
            user.companyprofile.employees = form.cleaned_data['employees']
            user.companyprofile.products = form.cleaned_data['products']
            user.companyprofile.sectors = form.cleaned_data['sectors']
            user.companyprofile.BOM_position = form.cleaned_data['BOM_position']
            user.companyprofile.linkedin_company = form.cleaned_data['linkedin_company']
            user.companyprofile.email_company = form.cleaned_data['email_company']
            user.companyprofile.save()
            return redirect('login_page')

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
