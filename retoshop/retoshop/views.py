from django.http import HttpResponse
from django.shortcuts import render
from Users.models import UserDetails

def Home(request):
    return render(request,"index.html")

def Register(request):
    return render(request,"register.html")
    
def Login(request):
    UserData = UserDetails.objects.all()
    return render(request,"login.html")

def Dashboard(request):
    return render(request,"dashboard.html")

def Contact(request):
    return render(request,"contact.html")

def Aboutus(request):
    return render(request,"aboutus.html")