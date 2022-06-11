from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def index_page(request):
    context = {}
    return render(request, 'home/index.html', context)


def home_page(request, pk):
    user = User.objects.get(id=pk)
    context = {'user': user}
    if request.user.is_authenticated and request.user.id == pk:
        return render(request, 'home/home.html', context)
    else:
        return redirect('login_page')
