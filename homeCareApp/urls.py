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
    path('service_form/<int:type_service>',views.service_form_page, name='add_service'),
    path('service_form/service_form/<int:type_service>',views.service_form_page),
    path('login_form',views.login_form),
    path('profile',views.profile),
    path('edit_profile',views.edit_user_form),
    path('delete_user',views.delete_user),
    path('delete_service/<int:service_id>',views.delete_service),
    path('carrer',views.carrer_page)

]