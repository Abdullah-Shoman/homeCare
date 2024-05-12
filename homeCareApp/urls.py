from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('services',views.service),
    path('aboutUs',views.aboutUs),
    path('main',views.coverpage)
]