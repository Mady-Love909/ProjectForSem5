from django.shortcuts import render,redirect
from datetime import datetime
from webstar.models import Info
from webstar.models import Feedback
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout ,login
# Create your views here.
# Password for Authentication website is Mayank333***
def index(request):
    if request.user.is_anonymous:
        messages.success(request,'WELCOME')
        return redirect("/login") 
    
    return render(request,'index.html')
    

def loginform(request):
    
    if request.method == "POST":
       name = request.POST.get('name')
       email = request.POST.get('email')
       dob = request.POST.get('dob')
       state = request.POST.get('state')
       mobno = request.POST.get('mobno')
       city = request.POST.get('city')
       district = request.POST.get('district')
       
       login = Info(name = name,email = email, state = state, mobno= mobno, city = city,district = district,dob=dob,date = datetime.today())
       login.save()
       messages.success(request, "Your message has been sent!")

    return render(request,'loginform.html') 
def contact(request):
    
    context = {
        'ph_no':'+91 82917 17187',
        'address':'media_gym123@gmail.com'
    }
    
    return render(request,'contact.html',context)
def blogs(request):
    
    return render(request,'blogs.html')


def feedback(request):
   

    if request.method == "POST":
        desc =  request.POST.get('desc')
        login = Feedback(desc = desc,date = datetime.today())
        login.save()

    
    return render(request,'feedback.html')

def loginUser(request):
    if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username,password)
            # check if user has entered  a correct credentials
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                # A backend authenticated the credentials
                return redirect("/")
            else:
                # No backend authenticated the credentials
                return render(request,'login.html')
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

def signup(request):
    return render(request,'signup.html')

# Create your views here.
