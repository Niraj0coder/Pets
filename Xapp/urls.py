from django.contrib import admin
from django.urls import path
from Xapp import views

urlpatterns = [
     path('',views.index,name="index"),
    path('index',views.index,name="index"),
    path('register',views.register,name="register"),
    path('loginuser',views.loginuser,name="loginuser"),
      path('About',views.About,name='about'),
     path('contact',views.contact,name='contact'),
      path('services',views.services,name='services'),
      path('sucess',views.sucess,name="sucess"),
         path('dog',views.dog,name="dog"),
            path('cat',views.cat,name="cat"),
               path('bird',views.bird,name="bird"),
               path('logoutuser',views.logoutuser, name='logoutuser') ,
    
]