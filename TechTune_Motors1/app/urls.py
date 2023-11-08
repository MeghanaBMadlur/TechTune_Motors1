from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.fun ,name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),

]