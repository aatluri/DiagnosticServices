# This is the urls file for the Django app called main. We link the primary urls in the website/urls.py to the urls here.
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('home', views.home, name='home'),
    path('signin', views.login_user, name='signin'),
    path('signout', views.logout_user, name='signout'),
]