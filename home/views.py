from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse


def index_page(request):
    context = {}
    return render(request, 'home/index.html', context)


def home_page(request, pk):
    if request.user.is_authenticated and request.user.id == pk:
        return redirect('radar_view_page', pk)
    else:
        return redirect('login_page')


def radar_view_page(request, pk):
    if request.user.is_authenticated and request.user.id == pk:
        user = User.objects.get(id=pk)
        context = {'user': user}
        return render(request, 'home/radar_view.html', context)
    else:
        return redirect('login_page')


def company_list_page(request, pk):
    if request.user.is_authenticated and request.user.id == pk:
        user = User.objects.get(id=pk)
        context = {'user': user}
        return render(request, 'home/company_list.html', context)
    else:
        return redirect('login_page')
