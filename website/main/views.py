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
    print("Entered Cardiac view")
    abnormaltests=None
    normaltests=None
    if request.user.id is not None:
        normaltests,abnormaltests = setcardiacpage_data()
    return render(request, 'main/cardiac.html',{
        "abnormaltests":abnormaltests,
        "normaltests":normaltests
    })


def test_detail(request,pathparameter):
    print("Entered test_detail view")
    print(pathparameter)
    testdetaildata=None
    recenttests=None
    if request.user.id is not None:
        testdetaildata,recenttests = settestdetail_data(testdetaildata,recenttests,pathparameter)
    if testdetaildata==None:
        print("Entered test_detail view->redirect view")
        return redirect(pathparameter)
    else:
        return render(request, 'main/testdetail.html',{
            "testdetaildata":testdetaildata,
            "recenttests":recenttests
        })



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
            "detaillink":"triglicerides",
        },
        "2" : {
            "name" : "Serum H.D.L. Cholesterol",
            "result":53,
            "unit":"mg/dl",
            "refinterval":"40 - 59",
            "date" : "May 25th, 2024",
            "status" : "Normal",
            "detaillink":"hdl",
        },
        "3" : {
            "name" : "Serum V.L.D.L. Cholesterol",
            "result":14,
            "unit":"mg/dl",
            "refinterval":"10 - 35",
            "date" : "May 25th, 2024",
            "status" : "Normal",
            "identificationnumber":50450206,
            "detaillink":"vldl",
        },
        "4" : {
            "name" : "Plasma Sugar Fasting",
            "result":79,
            "unit":"mgs/dl",
            "refinterval":"Fasting 70 - 110",
            "date" : "May 25th, 2024",
            "status" : "Normal",
            "detaillink":"plasmasugarfasting",
        },
    }
   abnormaltests = {
        "1" : {
            "name" : "Serum Cholesterol",
            "result":221,
            "unit":"mg/dl",
            "refinterval":"Less than 200",
            "date" : "May 25th, 2024",
            "status" : "Abnormal",
            "detaillink":"serumcholestrol"
        },
        "2" : {
            "name" : "Serum L.D.L. Cholesterol",
            "result":154,
            "unit":"mg/dl",
            "refinterval":"Less than 130",
            "date" : "May 25th, 2024",
            "status" : "Abnormal",
            "detaillink":"serumldlcholestrol"
            },
        "3" : {
            "name" : "Serum Urea",
            "result":44,
            "unit":"mg/dl",
            "refinterval":"17 - 43",
            "date" : "May 25th, 2024",
            "status" : "Abnormal",
            "detaillink":"serumurea"
        },
        "4" : {
            "name" : "Glycosylated Haemoglobin (HbA1c)",
            "result":5.7,
            "unit":"%",
            "refinterval":"Below 5.7",
            "date" : "May 25th, 2024",
            "status" : "Abnormal",
            "detaillink":"glycosylatedhaemoglobin"
        },
    }
   return normaltests,abnormaltests

def settestdetail_data(testdetaildata,recenttests,pathparameter):
   if(pathparameter=="triglicerides"):
        testdetaildata = {
                    "name" : "Serum Triglycerides",
                    "result":68,
                    "unit":"mg/dl",
                    "refinterval":"Optimal - 30-149 ,Boarder-line High 150 – 199 mg/dL ,High 200 - 399 mg/dL ,Very High > 400 mg/dL",
                    "date" : "May 25th, 2024",
                    "status" : "Normal",
                    "methodology":"Lipase GK: GPO POD",
                    "description":"Triglycerides are an important measure of heart health. High triglycerides may contribute to hardening of the arteries or thickening of the artery walls (arteriosclerosis) — which increases the risk of stroke, heart attack and heart disease ."
        }
        recenttests = {
                "1" : {
                    "name" : "Serum Triglycerides",
                    "result":68,
                    "unit":"mg/dl",
                    "refinterval":"Fasting 30-149",
                    "date" : "May 25th, 2024",
                    "status" : "Normal",
                    "identificationnumber":50450206,
                    "description":"Triglycerides are an important measure of heart health. High triglycerides may contribute to hardening of the arteries or thickening of the artery walls (arteriosclerosis) — which increases the risk of stroke, heart attack and heart disease .",
                    "detaillink":"triglicerides"
                },
                "2" : {
                    "name" : "Serum H.D.L. Cholesterol",
                    "result":53,
                    "unit":"mg/dl",
                    "refinterval":"40-59",
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
   return testdetaildata,recenttests

