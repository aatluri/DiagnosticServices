from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm

# Create your views here.


def index(request):
    return render(request, 'main/index.html')

def cardiac(request):
    abnormaltests=None
    normaltests=None
    if request.user.id is not None:
        normaltests,abnormaltests = setcardiacpage_data()
    return render(request, 'main/cardiac.html',{
        "abnormaltests":abnormaltests,
        "normaltests":normaltests
    })


def test_detail(request,pathparameter):
    if pathparameter=="triglicerides":
        testdetaildata=None
        if request.user.id is not None:
            testdetaildata = settestdetail_data()
        return render(request, 'main/testdetail.html',{
            "testdetaildata":testdetaildata
        })
    else:
        return redirect(pathparameter)


def home(request):
    print(request.user.id)
    overallhealthstatus=None
    overduetests=None
    recenttests=None
    abnormaltests=None
    normaltests=None
    if request.user.id is not None:
        overallhealthstatus,overduetests,recenttests,abnormaltests,normaltests = sethomepage_data()
    return render(request, 'main/home.html',{
        "overallhealthstatus":overallhealthstatus,
        "overduetests":overduetests,
        "recenttests":recenttests,
        "abnormaltests":abnormaltests,
        "normaltests":normaltests
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



def sethomepage_data():
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
    recenttests = {
            "1" : {
                "name" : "Plasma Sugar 2 Hr Post Breakfast",
                "date" : "May 25th, 2024",
                "img" : "cardiac",
            },
            "2" : {
                "name" : "Serum Urea",
                "date" : "May 25th, 2024",
                "img" : "cardiac",
            },
            "3" : {
                "name" : "Serum Creatine",
                "date" : "May 25th, 2024",
                "img" : "cardiac",
            }
        }
    abnormaltests = {
        "1" : {
            "name" : "Glycosylated Haemoglobin (HbA1c)",
            "result":221,
            "unit":"mg/dl",
            "refinterval":"Below 5.7",
            "date" : "May 25th, 2024",
            "status" : "abnormal",
            "identificationnumber":50450206,
        },
        "2" : {
            "name" : "Glycosylated Haemoglobin (HbA1c)",
            "result":221,
            "unit":"mg/dl",
            "refinterval":"Below 5.7",
            "date" : "May 25th, 2024",
            "status" : "abnormal",
            "identificationnumber":50450206,
        },
        "3" : {
            "name" : "Glycosylated Haemoglobin (HbA1c)",
            "result":221,
            "unit":"mg/dl",
            "refinterval":"Below 5.7",
            "date" : "May 25th, 2024",
            "status" : "abnormal",
            "identificationnumber":50450206,
        },
    }
    normaltests = {
        "1" : {
            "name" : "Glycosylated Haemoglobin (HbA1c)",
            "result":221,
            "unit":"mg/dl",
            "refinterval":"Below 5.7",
            "date" : "May 25th, 2024",
            "status" : "abnormal",
            "identificationnumber":50450206,
        },
        "2" : {
            "name" : "Glycosylated Haemoglobin (HbA1c)",
            "result":221,
            "unit":"mg/dl",
            "refinterval":"Below 5.7",
            "date" : "May 25th, 2024",
            "status" : "abnormal",
            "identificationnumber":50450206,
        },
        "3" : {
            "name" : "Glycosylated Haemoglobin (HbA1c)",
            "result":221,
            "unit":"mg/dl",
            "refinterval":"Below 5.7",
            "date" : "May 25th, 2024",
            "status" : "abnormal",
            "identificationnumber":50450206,
        },
    }
    return overallhealthstatus,overduetests,recenttests,abnormaltests,normaltests

def setcardiacpage_data():
   normaltests = {
        "1" : {
            "name" : "Serum Triglycerides",
            "result":68,
            "unit":"mg/dl",
            "refinterval":"Fasting 30-149",
            "date" : "May 25th, 2024",
            "status" : "Normal",
            "identificationnumber":50450206,
            "description":"Triglycerides are an important measure of heart health. High triglycerides may contribute to hardening of the arteries or thickening of the artery walls (arteriosclerosis) — which increases the risk of stroke, heart attack and heart disease ."
        },
        "2" : {
            "name" : "Serum Triglycerides",
            "result":68,
            "unit":"mg/dl",
            "refinterval":"Fasting 30-149",
            "date" : "May 25th, 2024",
            "status" : "Normal",
            "identificationnumber":50450206,
            "description":"Triglycerides are an important measure of heart health. High triglycerides may contribute to hardening of the arteries or thickening of the artery walls (arteriosclerosis) — which increases the risk of stroke, heart attack and heart disease ."
        },
        "3" : {
            "name" : "Serum Triglycerides",
            "result":68,
            "unit":"mg/dl",
            "refinterval":"Fasting 30-149",
            "date" : "May 25th, 2024",
            "status" : "Normal",
            "identificationnumber":50450206,
            "description":"Triglycerides are an important measure of heart health. High triglycerides may contribute to hardening of the arteries or thickening of the artery walls (arteriosclerosis) — which increases the risk of stroke, heart attack and heart disease ."
        },
        "4" : {
            "name" : "Serum Triglycerides",
            "result":68,
            "unit":"mg/dl",
            "refinterval":"Fasting 30-149",
            "date" : "May 25th, 2024",
            "status" : "Normal",
            "identificationnumber":50450206,
            "description":"Triglycerides are an important measure of heart health. High triglycerides may contribute to hardening of the arteries or thickening of the artery walls (arteriosclerosis) — which increases the risk of stroke, heart attack and heart disease ."
        },
    }
   abnormaltests = {
        "1" : {
            "name" : "Serum Triglycerides",
            "result":68,
            "unit":"mg/dl",
            "refinterval":"Fasting 30-149",
            "date" : "May 25th, 2024",
            "status" : "Abnormal",
            "identificationnumber":50450206,
            "description":"Triglycerides are an important measure of heart health. High triglycerides may contribute to hardening of the arteries or thickening of the artery walls (arteriosclerosis) — which increases the risk of stroke, heart attack and heart disease ."
        },
        "2" : {
            "name" : "Serum Triglycerides",
            "result":68,
            "unit":"mg/dl",
            "refinterval":"Fasting 30-149",
            "date" : "May 25th, 2024",
            "status" : "Abnormal",
            "identificationnumber":50450206,
            "description":"Triglycerides are an important measure of heart health. High triglycerides may contribute to hardening of the arteries or thickening of the artery walls (arteriosclerosis) — which increases the risk of stroke, heart attack and heart disease ."
        },
        "3" : {
            "name" : "Serum Triglycerides",
            "result":68,
            "unit":"mg/dl",
            "refinterval":"Fasting 30-149",
            "date" : "May 25th, 2024",
            "status" : "Abnormal",
            "identificationnumber":50450206,
            "description":"Triglycerides are an important measure of heart health. High triglycerides may contribute to hardening of the arteries or thickening of the artery walls (arteriosclerosis) — which increases the risk of stroke, heart attack and heart disease ."
        },
        "4" : {
            "name" : "Serum Triglycerides",
            "result":68,
            "unit":"mg/dl",
            "refinterval":"Fasting 30-149",
            "date" : "May 25th, 2024",
            "status" : "Abnormal",
            "identificationnumber":50450206,
            "description":"Triglycerides are an important measure of heart health. High triglycerides may contribute to hardening of the arteries or thickening of the artery walls (arteriosclerosis) — which increases the risk of stroke, heart attack and heart disease ."
        },
    }
   return normaltests,abnormaltests

def settestdetail_data():
   testdetaildata = {
        "1" : {
            "name" : "Serum Triglycerides",
            "result":68,
            "unit":"mg/dl",
            "refinterval":"Fasting 30-149",
            "date" : "May 25th, 2024",
            "status" : "Normal",
            "identificationnumber":50450206,
            "description":"Triglycerides are an important measure of heart health. High triglycerides may contribute to hardening of the arteries or thickening of the artery walls (arteriosclerosis) — which increases the risk of stroke, heart attack and heart disease ."
        },
        "2" : {
            "name" : "Serum Triglycerides",
            "result":68,
            "unit":"mg/dl",
            "refinterval":"Fasting 30-149",
            "date" : "May 25th, 2024",
            "status" : "Normal",
            "identificationnumber":50450206,
            "description":"Triglycerides are an important measure of heart health. High triglycerides may contribute to hardening of the arteries or thickening of the artery walls (arteriosclerosis) — which increases the risk of stroke, heart attack and heart disease ."
        },
        "3" : {
            "name" : "Serum Triglycerides",
            "result":68,
            "unit":"mg/dl",
            "refinterval":"Fasting 30-149",
            "date" : "May 25th, 2024",
            "status" : "Normal",
            "identificationnumber":50450206,
            "description":"Triglycerides are an important measure of heart health. High triglycerides may contribute to hardening of the arteries or thickening of the artery walls (arteriosclerosis) — which increases the risk of stroke, heart attack and heart disease ."
        },
        "4" : {
            "name" : "Serum Triglycerides",
            "result":68,
            "unit":"mg/dl",
            "refinterval":"Fasting 30-149",
            "date" : "May 25th, 2024",
            "status" : "Normal",
            "identificationnumber":50450206,
            "description":"Triglycerides are an important measure of heart health. High triglycerides may contribute to hardening of the arteries or thickening of the artery walls (arteriosclerosis) — which increases the risk of stroke, heart attack and heart disease ."
        },
    }
   return testdetaildata

