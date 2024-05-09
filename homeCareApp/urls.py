from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('about_us',views.aboutus),
    path('cover_page',views.coverpage),
]