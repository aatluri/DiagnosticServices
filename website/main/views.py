from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


def home(request):
    return render(request, 'main/index.html')


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
            return redirect('signin')

    else:
        return render(request,'authentication/login.html')

def logoutUser(request):
    logout(request)
    return render(request,'authentication/login.html')
