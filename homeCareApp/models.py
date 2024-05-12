from django.db import models
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

class User(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=70 , unique=True)
    password = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

