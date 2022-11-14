from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact, name = 'contact'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('consultation', views.consultation, name='consultation'),
    path('ambulance', views.ambulance, name='ambulance'),
    path('AR_tut', views.AR_tut, name='AR_tut'),
]