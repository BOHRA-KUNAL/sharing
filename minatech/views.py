from django.shortcuts import render,redirect
from . models import *

# Create your views here.

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def register(request):
    return render(request,'register.html')
# def contact(request):
#     return render(request,'contact.html')

def contact(request):
    if request.method=="POST":
        print(request)
        name=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']
        print(name,lastname,email)
        obj=Contact(name=name,email=email,phone=phone,desc=desc).save()
        return redirect('/contact')
    else:
        return render(request, "contact.html")

def course(request):
    a=courses.objects.all()
    context={'data':a}
    return render(request,'courses.html',context)
def blog(request):
    b=blogs.objects.all()
    context={'data':b}
    return render(request,'blog.html',context)






