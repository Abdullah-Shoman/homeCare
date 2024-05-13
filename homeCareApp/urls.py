from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('services',views.service),
    path('aboutUs',views.aboutUs),
    path('login',views.login_page),
    path('registration',views.registration_page),
    path('logout',views.logout_view),
    path('registration_form',views.registration_form, name='reg'),
    path('service_form',views.service_form_page),
    path('login_form',views.login_form)

]