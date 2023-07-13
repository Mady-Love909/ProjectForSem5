from django.contrib import admin
from django.urls import path
from webstar import views
urlpatterns = [
    
    path('',views.index,name="index"),
    path('loginform',views.loginform,name="loginform"),
    path('contact',views.contact,name="contact"),
    path('blogs',views.blogs,name="blogs"),
    path('feedback',views.feedback,name="feedback")
]
