from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"homePage.html")
def logIn(request):
    return render(request,"logInPage.html")
def signUp(request):
    return render(request,"signUpPage.html")
def home(request):
    return render(request,"homePage.html")
def profile(request):
    return render(request,"profilePage.html")