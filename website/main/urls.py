# This is the urls file for the Django app called main. We link the primary urls in the website/urls.py to the urls here.
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
]