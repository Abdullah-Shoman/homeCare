from django.shortcuts import render , redirect
from django.contrib.auth import logout
from . import models
from django.contrib import messages
import bcrypt
# Create your views here.
def index(request):    
    if 'user_id' in request.session:
        context = {
            'user': models.get_user_by_id(request.session['user_id'])
        }
        return render(request,'coverpage.html',context)
    else:
            return render(request,'coverpage.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def service(request):
    return render(request,'services.html')

def aboutUs(request):
    return render(request,'aboutus.html')

def login_page(request):
    return render(request,'login_form.html')

def login_form(request):
    if request.method == 'POST':
        login_error = models.User.objects.basic_validator_login(request.POST)
        if len(login_error) > 0:
            for key, value in login_error.items():
                messages.error(request, value,extra_tags='login_error')
            return redirect('/login')
        # get the registered user from DB
        registered_user = models.get_user_by_email(request.POST)
        if registered_user:
            logged_user = registered_user[0]
            # check the password
            if bcrypt.checkpw(request.POST['registered_password'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                return redirect('/')
            else:
                messages.error(request,'The User Email or Password is Incorrect',extra_tags='login_error')
                return redirect(login_page)
        else:    
            messages.error(request,'The User Email or Password is Incorrect',extra_tags='login_error')
        
    return redirect('/')


def registration_page(request):
    return render(request,'registration_form.html')


def registration_form(request):
    if request.method == 'POST':
        # validation form
        register_error = models.User.objects.basic_validator_register(request.POST)
        if len(register_error) > 0:
            for key, value in register_error.items():
                messages.error(request, value,extra_tags='registration_error')
            return redirect('/registration')
        print('good')
        # hash password using bcrypt 
        password = request.POST['form_password']
        # should save pw_hash in the database
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        # handel the unique email error 
        try:
            models.create_user(request.POST,pw_hash)
        except:
            messages.error(request,'Do you already have an account?',extra_tags='registration_error')

    return redirect('/')

def service_form_page(request):
    return render(request,'service_form.html')