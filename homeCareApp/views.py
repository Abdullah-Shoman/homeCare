from django.shortcuts import render , redirect

# Create your views here.
def index(request):
    return render(request,'coverpage.html')

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