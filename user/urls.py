from django.conf.urls.static import static
from django.urls import path
from project import settings
from . import views

urlpatterns = [
    path('', views.login_page_redirect),
    path('login', views.login_page, name='login_page'),
    path('logout', views.logout_page, name='logout_page'),
    path('signup_1', views.signup_page_1, name='signup_page_1'),
    path('signup_2', views.signup_page_2, name='signup_page_2'),
    path('signup_3', views.signup_page_3, name='signup_page_3'),
]
# static is to use only in debug!!
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
