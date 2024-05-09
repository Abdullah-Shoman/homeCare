from django.shortcuts import render , redirect

# Create your views here.
def index(request):
    return render(request,'index.html')

def aboutus(request):
    return render(request,'aboutus.html')

def coverpage(request):
    return render(request,'coverpage.html')