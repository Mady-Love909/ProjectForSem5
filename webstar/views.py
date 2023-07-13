from django.shortcuts import render
from datetime import datetime
from webstar.models import Info
from webstar.models import Feedback
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'index.html')

def loginform(request):
    messages.success(request,'This is message for success')
    if request.method == "POST":
       name = request.POST.get('name')
       state = request.POST.get('state')
       mobno = request.POST.get('mobno')
       city = request.POST.get('city')
       district = request.POST.get('district')
       
       login = Info(name = name,state = state, mobno= mobno, city = city,district = district,date = datetime.today())
       login.save()
       messages.success(request, "Your message has been sent")

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


# Create your views here.
