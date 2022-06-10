from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page_redirect),
    path('login', views.login_page, name='login_page'),
    path('logout', views.logout_page, name='logout_page'),
    path('signup', views.signup_page, name='signup_page'),
]
