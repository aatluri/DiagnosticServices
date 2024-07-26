# This is the urls file for the Django app called main. We link the primary urls in the website/urls.py to the urls here.
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('home2', views.home2, name='home2'),
    path('signin', views.login_user, name='signin'),
    path('signout', views.logout_user, name='signout'),
]