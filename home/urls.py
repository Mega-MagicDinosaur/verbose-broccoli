from django.conf.urls.static import static
from django.urls import path
from project import settings
from . import views

urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('<int:pk>', views.home_page, name='home_page'),
]
# static is to use only in debug!!
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
