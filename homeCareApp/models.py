from django.db import models
from django.contrib.auth.models import User as auth_user
import re

# Create your models here.
class UserManager(models.Manager):
    def basic_validator_register(self,postData):
        errors = {}

            # first name validation
        if len(postData['form_first_name']) < 5 :
            errors['first_name'] = 'First Name should be at lest 5 character'

            # last name validaion
        if len(postData['form_last_name']) < 5 :
            errors['last_name_alpha'] = 'Last name should be at least 5 character'

        if len(postData['form_phone_number']) < 10 :
            errors['phone_number'] = 'phone Number should be at least 10 character'

            # email Validation
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['form_email']):
            errors['email'] = 'Invalid email Address!'

            # password validation
        if  len(postData['form_password']) < 7:
            errors['password'] = 'Password should be more than 7 character'
        if not postData['form_password'] == postData['form_confirm_pw']:
            errors['confirm_password'] = 'Confirm Password not match Password'
        return errors
    
    def basic_validator_login(self,postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['registered_email']):
            errors['email'] = 'Invalid Email Address!'
        return errors
    

class User(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=70 , unique=True)
    password = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()



#  ------------  CRAD User -----------  #
def create_user(postData,password):
    user_first_name = postData['form_first_name']
    user_last_name = postData['form_last_name']
    user_email = postData['form_email']
    user_phone_number = int(postData['form_phone_number'])
    user_password = password
    User.objects.create(first_name = user_first_name,
                        last_name = user_last_name,
                        email = user_email,
                        password = user_password,
                        phone_number = user_phone_number)
    # auth_user.objects.create(password = user_password,
    #                         is_superuser = False ,
    #                         username = user_first_name ,
    #                         last_name = user_last_name,
    #                         email = user_email,
    #                         is_staff = False ,
    #                         is_active = True,
    #                         first_name = user_first_name)
    return get_reg_user_by_email(user_email)
    
def get_user_by_email(postData):
    registered_user = User.objects.filter(email = postData['registered_email'])
    return registered_user

def get_reg_user_by_email(email):
    registered_user = User.objects.filter(email = email)
    return registered_user

def get_user_by_id(user_id):
    user = User.objects.get(id = user_id)
    return user

def edit_user(postData,password,user_id):
    edit_user = get_user_by_id(user_id)
    edit_user.first_name = postData['form_first_name']
    edit_user.last_name = postData['form_last_name']
    edit_user.email = postData['form_email']
    edit_user.phone_number = postData['form_phone_number']
    edit_user.password = password
    edit_user.save()

def delete_user(user_id):
    del_user = get_user_by_id(user_id)
    del_user.delete()