from django.contrib import admin
from django.urls import path
from webstar import views
urlpatterns = [
    
    path('',views.index,name="index"),
    path('loginform',views.loginform,name="loginform"),
    path('contact',views.contact,name="contact"),
    path('blogs',views.blogs,name="blogs"),
    path('feedback',views.feedback,name="feedback"),
    path('login',views.loginUser,name="loginUser"),
    path('logoutUser',views.logoutUser,name="logoutUser"),
    path('signup',views.signup,name="signup")
]
