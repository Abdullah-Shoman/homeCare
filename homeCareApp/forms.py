from typing import Any, Mapping
from django import forms
import datetime
from django.forms import ModelForm
from django.forms.renderers import BaseRenderer
import re
SERVICES_CHOICES = [
        ('Home Nursing','Home Nursing'),
        ('Physical Therapy','physical Therapy'),
        ('Speical Needs', 'Special Needs') 
    ]
CHOICES_GENDER = (
    ("Male", "Male"),
    ("Female", "Female")
    )
CHOICES_PERIOD = (
    ('8:00 AM to 16:00 PM','8:00 AM to 16:00 PM'),
    ('16:00 PM to 12:00 AM','16:00 PM to 12:00 AM'),
    ('12:00 AM to 8:00 AM','12:00 AM to 8:00 AM')
)

# CHOICES_PERIOD = {"8:00 AM to 16:00 PM": "8:00 AM to 16:00 PM", "16:00 PM to 12:00 AM": "16:00 PM to 12:00 AM", "12:00 AM to 8:00 AM": "12:00 AM to 8:00 AM"}


class services_form(forms.Form):
    date_now = datetime.datetime.now().strftime('%Y-%m-%d')
    service_type = forms.ChoiceField(choices=SERVICES_CHOICES )
    name_patient = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    age =forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Age', 'style': 'width: 300px;', 'class': 'form-control'}))
    gender = forms.ChoiceField(widget=forms.RadioSelect(attrs={'placeholder': 'gender', 'class': 'form-check d-flex '}),choices=CHOICES_GENDER)
    city =forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'city', 'style': 'width: 300px;', 'class': 'form-control'}))
    location =forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Location', 'style': 'width: 300px;', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'style': 'width: 300px;', 'class': 'form-control'}))
    phone_number =forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Phone Number', 'style': 'width: 300px;', 'class': 'form-control'}))
    start_date = forms.DateField(
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date",'style': 'width: 300px;','class': 'form-control','min':date_now}),
        input_formats=["%Y-%m-%d"]
    )
    period = forms.ChoiceField(widget=forms.RadioSelect,choices=CHOICES_PERIOD)
    time = forms.TimeField(required=True,
        widget=forms.DateInput(format="%H:%M", attrs={"type": "time",'style': 'width: 300px;', 'class': 'form-control'}),
        input_formats=["%H:%M"]
    )

    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data

    def clean_start_date(self):
        cleaned_data = self.cleaned_data
        start_date = cleaned_data['start_date']
        # print('start_date',start_date)
        # print(start_date.strftime('%Y'))
        date = datetime.datetime.now()
        day = int(date.strftime('%d'))+5
        if start_date.strftime('%Y') < date.strftime('%Y'):
            self.add_error('start_date',"Invalid Year")
        if start_date.strftime('%m') < date.strftime('%m'):
            self.add_error('start_date',"Invalid Month")
        if start_date.strftime('%d') < str(day):
            self.add_error('start_date',"Invalid Day")
        return start_date

    def clean_name_patient(self):
        cleaned_data = self.cleaned_data
        name_patient = cleaned_data['name_patient']
        if len(name_patient) < 5 : 
            self.add_error('name_patient',"Name should be at least 5 character")
        return name_patient
    
    def clean_age(self):
        cleaned_data = self.cleaned_data
        cleaned_age = cleaned_data['age']
        if cleaned_age <= 0 : 
            self.add_error('age',"Invalid Age !")
        return cleaned_age
    
    def clean_city(self):
        cleaned_data = self.cleaned_data
        cleaned_city = cleaned_data['city']
        if len(cleaned_city) < 5 : 
            self.add_error('city',"Enter City Full Name")
        return cleaned_city
    
    def clean_location(self):
        cleaned_data = self.cleaned_data
        cleaned_location = cleaned_data['location']
        if len(cleaned_location) < 5 : 
            self.add_error('location',"Enter Full Location")
        return cleaned_location

    def clean_email(self):
        cleaned_data = self.cleaned_data
        cleaned_email = cleaned_data['email']
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(cleaned_email):
            self.add_error('email',"Invalid Email")
        return cleaned_email

    # def clean_phone_number(self):
    #     cleaned_data = self.cleaned_data
    #     cleaned_phone_number = cleaned_data['phone_number']
    #     if not EMAIL_REGEX.match(cleaned_email):
    #         self.add_error('email',"Invalid Email")
    #     return cleaned_email





# while num != 0:
#     num //= 10
#     count += 1


#  EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
#         if not EMAIL_REGEX.match(postData['form_email']):
#             errors['email'] = 'Invalid email Address!'
    # service_type = forms.MultipleChoiceField(
    #     required=False,
    #     widget=forms.CheckboxSelectMultiple,
    #     choices=SERVICES_CHOICES,
    # 


