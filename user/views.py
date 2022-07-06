from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from user.forms import *


def login_page_redirect(request):
    return redirect('login_page')


@csrf_protect
def signup_page_1(request):
    exceptions = {
        'license_agreement_exc': False,
        'taken_username_exc': False,
        'password_validation_exc': False
    }  # use this in 2 and 3 later
    if request.method == 'POST':
        email = request.POST.get('email', 'none')
        password = request.POST.get('password', 'none')
        confirm = request.POST.get('password_confirmation', '')  # password and confirm default preferably different
        license_agreement = request.POST.getlist('license_agreement')

        # validate
        if User.objects.filter(username=email):
            exceptions['taken_username_exc'] = True
        if password != confirm:
            exceptions['password_validation_exc'] = True
        if len(license_agreement) == 0:
            exceptions['license_agreement_exc'] = True

        if all(value == False for value in exceptions.values()):
            User.objects.create_user(username=email, password=password)  # EMAIL IS USED AS A USERNAME!!
            request.session['email'] = email
            return redirect('signup_page_2')

    context = {'exceptions': exceptions}
    return render(request, 'user/signup1.html', context)


def signup_page_2(request):
    exceptions = {'unfilled_form_exc': False}
    if request.method == 'POST':
        user = User.objects.get(username=request.session.get('email', ''))
        data = {
            'name': request.POST.get('name', 'none'),
            'surname': request.POST.get('surname', 'none'),
            'username': request.POST.get('username', 'none'),
            'phone_prefix': request.POST.get('phone_prefix', 'none'),
            'phone_number': request.POST.get('phone_number', 'none'),
            'linkedin_profile': request.POST.get('linkedin_profile', 'none'),
            'company': request.POST.get('company', 'none'),
            'department': request.POST.get('department', 'none'),
            'job_title': request.POST.get('job_title', 'none')
        }

        # validate
        if not all(value != '' for value in data.values()):
            exceptions['unfilled_form_exc'] = True

        if all(value == False for value in exceptions.values()):
            user.userprofile.name = data['name']
            user.userprofile.surname = data['surname']
            user.userprofile.username = data['username']
            user.userprofile.prefix = data['phone_prefix']
            user.userprofile.number = data['phone_number']
            user.userprofile.linkedin_user = data['linkedin_profile']
            user.userprofile.company = data['company']
            user.userprofile.department = data['department']
            user.userprofile.job_title = data['job_title']
            user.userprofile.save()
            return redirect('signup_page_3')

    context = {'exceptions': exceptions}
    return render(request, 'user/signup2.html', context)


def signup_page_3(request):
    exceptions = {'unfilled_form_exc': False}
    if request.method == 'POST':
        user = User.objects.get(username=request.session['email'])

        data = {
            'type_of_code': request.POST.get('type_of_code', 'none'),
            'code': request.POST.get('code', 'none'),
            'address': request.POST.get('address', 'none'),
            'turnover': request.POST.get('turnover', 'none'),
            'employees': request.POST.get('employees', 'none'),
            'products': request.POST.get('products', 'none'),
            'sectors': request.POST.get('sectors', 'none'),
            'bom_position': request.POST.get('bom_position', 'none'),
            'company_linkedin_profile': request.POST.get('company_linkedin_profile', 'none'),
            'company_email': request.POST.get('company_email', 'none')
        }

        if not all(value != '' for value in data.values()):
            exceptions['unfilled_form_exc'] = True

        if all(value == False for value in exceptions.values()):
            user.companyprofile.type_of_code = data['type_of_code']
            user.companyprofile.code = data['code']
            user.companyprofile.address = data['address']
            user.companyprofile.turnover = data['turnover']
            user.companyprofile.employees = data['employees']
            user.companyprofile.products = data['products']
            user.companyprofile.sectors = data['sectors']
            user.companyprofile.BOM_position = data['bom_position']
            user.companyprofile.linkedin_company = data['company_linkedin_profile']
            user.companyprofile.email_company = data['company_email']
            user.companyprofile.save()
            return redirect('login_page')

    context = {'exceptions': exceptions}
    return render(request, 'user/signup3.html', context)


@csrf_protect
def login_page(request):
    exceptions = {'auth_failed_exc': False}
    if request.method == 'POST':
        email = request.POST.get('email', 'none')
        password = request.POST.get('password', 'none')
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user=user)
            return redirect('home_page', user.id)
        else:
            exceptions['auth_failed_exc'] = True
    context = {'exceptions': exceptions}
    return render(request, 'user/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('index_page')
