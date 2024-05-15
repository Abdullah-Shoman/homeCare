from django.shortcuts import render , redirect
from django.contrib.auth import logout
from . import models
from django.contrib import messages
import bcrypt
from django.contrib.auth.models import User as auth_user
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'coverpage.html')

def logout_view(request):
    logout(request)
    if 'user_id' in request.session:
        del request.session['user_id']
        del request.session['user_name']
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
                request.session['user_name'] = logged_user.first_name
                return redirect('/')
            else:
                messages.error(request,'The User Email or Password is Incorrect',extra_tags='login_error')
                return redirect(login_page)
        else:    
            messages.error(request,'The User Email or Password is Incorrect',extra_tags='login_error')
            return redirect('/login')
    return redirect('/')


def registration_page(request):
    return render(request,'registration_form.html')

# here need update!!!!!!!!!!!!
def registration_form(request):
    if request.method == 'POST':
        # validation form
        register_error = models.User.objects.basic_validator_register(request.POST)
        if len(register_error) > 0:
            for key, value in register_error.items():
                messages.error(request, value,extra_tags='registration_error')
                # here need update!!!!!!!!!!!!
            # return redirect('/registration')
            data = 'error'
            return HttpResponse(data)
        print('good')
        # hash password using bcrypt 
        password = request.POST['form_password']
        # should save pw_hash in the database
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        # handel the unique email error 
        register_user_list = models.create_user(request.POST,pw_hash)
        register_user = register_user_list[0]
        request.session['user_id'] = register_user.id
        request.session['user_name'] = register_user.first_name
        return redirect(service)
    return redirect('/')

def service_form_page(request):
    return render(request,'service_form.html')

def profile(request):
    if 'user_id' in request.session:
        context = {
            'user': models.get_user_by_id(request.session['user_id'])
        }
        return render(request,'profile.html',context)
    elif auth_user.is_authenticated:
        return render(request,'complite_reg.html')
    
    return redirect('/')

def edit_user_form(request):
    if request.method == 'POST':
        # validation form
        register_error = models.User.objects.basic_validator_register(request.POST)
        if len(register_error) > 0:
            for key, value in register_error.items():
                messages.error(request, value,extra_tags='edit_error')
        registered_user = models.get_reg_user_by_email(request.POST['form_email'])
        if registered_user:
            logged_user = registered_user[0]
            # check the password
            if bcrypt.checkpw(request.POST['current_password'].encode(), logged_user.password.encode()):
                print('update pasword')
            else:
                messages.error(request,'The Current Password is Incorrect',extra_tags='edit_error')
                return redirect(profile)
            password = request.POST['form_password']
            # should save pw_hash in the database
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            models.edit_user(request.POST,pw_hash,request.session['user_id'])
            messages.error(request,'Profile Updated',extra_tags='edit_error')
            return redirect(profile)
    return redirect('/')

def delete_user(request):
    if request.method == 'POST':
        models.delete_user(request.session['user_id'])
        logout_view(request)
        return redirect('/')
    return redirect(profile)