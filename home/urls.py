from django.conf.urls.static import static
from django.urls import path
from project import settings
from . import views

urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('<int:pk>', views.home_page, name='home_page'),
    path('<int:pk>/radar_view', views.radar_view_page, name='radar_view_page'),
    path('<int:pk>/company_list', views.company_list_page, name='company_list_page'),
]
# static is to use only in debug!!
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
