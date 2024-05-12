from django.shortcuts import render , redirect
from django.contrib.auth import logout

# Create your views here.
def index(request):
    
    return render(request,'coverpage.html')

def logout_view(request):
    logout(request)
    return redirect('/')


def service(request):
    return render(request,'services.html')

def aboutUs(request):
    return render(request,'aboutus.html')

def coverpage(request):
    return render(request,'coverpage.html')

def login_page(request):
    return render(request,'login_form.html')

def registration_page(request):
    return render(request,'registration_form.html')
