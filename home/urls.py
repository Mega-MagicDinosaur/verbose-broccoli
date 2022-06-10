from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('/<str:pk>', views.home_page, name='home_page'),
]
