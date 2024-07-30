from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm

# Create your views here.


def index(request):
    return render(request, 'main/index.html')

def home(request):
    print(request.user.id)
    overallhealthstatus=None
    overduetests=None
    if request.user.id is not None:
        overallhealthstatus = {
            "cardiac":"Good",
            "diabetes":"Warning",
            "thyroid":"Danger",
            "liver":"Good",
            "kidney":"Good",
            "blood":"Good",
            "vitamin":"Good",
            "gastro":"Good",
            "cancer":"Good",
            "arthritis":"Good",
            "anemia":None,
            "prenatal":None,
        }
        overduetests = {
            "1" : {
                "name" : "Plasma Sugar Fasting",
                "date" : "May 25th, 2022",
                "img" : "cardiac",
            },
            "2" : {
                "name" : "Plasma Sugar Fasting",
                "date" : "May 25th, 2022",
                "img" : "cardiac",
            },
            "3" : {
                "name" : "Plasma Sugar Fasting",
                "date" : "May 25th, 2022",
                "img" : "cardiac",
            }
        }
    return render(request, 'main/home.html',{
        "overallhealthstatus":overallhealthstatus,
        "overduetests":overduetests
    })


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


def register_user(request):
    print("Entered register user")
    if request.method == "POST":
        form=RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect('home')
    else:
        form = RegisterUserForm()

    return render(request, 'authentication/register_user.html', {
        "form":form,
    })

