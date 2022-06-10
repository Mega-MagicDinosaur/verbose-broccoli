from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
from django.views.decorators.csrf import csrf_protect


def login_page_redirect(request):
    return redirect('login_page')


@csrf_protect
def signup_page(request):
    create = True
    exceptions = {'taken_username_exc': False, 'empty_field_exc': False, 'confirm_password_exc': False, }
    context = {'exceptions': exceptions}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')
        if not (username and password and confirm):
            exceptions['empty_field_exc'] = True
            create = False
        if not (password == confirm):
            exceptions['confirm_password_exc'] = True
            create = False
        if User.objects.filter(username=username):
            exceptions['taken_username_exc'] = True
            create = False
        if create:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('login_page')
    return render(request, 'user/signup.html', context)


@csrf_protect
def login_page(request):
    exceptions = {'filled_fields_exc': False, 'wrong_fields_exc': False, }
    context = {'exceptions': exceptions}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page', username)
        else:
            if not (username and password):
                exceptions['empty_field_exc'] = True
            else:
                exceptions['wrong_fields_exc'] = True
    return render(request, 'user/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('index_page')
