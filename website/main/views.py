from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


def index(request):
    return render(request, 'main/index.html')

def home(request):
    return render(request, 'main/home.html')


def login_user(request):
    print("entered login_user")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            print("entered user is not None")
            login(request,user)
            return redirect('home')
        else:
            print("entered user is none")
            messages.success(request, ("There Was An Error Logging In, Try Again..."))
            return redirect('signin')

    else:
        return render(request,'authentication/login.html')

def logout_user(request):
    print("logout_user")
    logout(request)
    return redirect('home')
