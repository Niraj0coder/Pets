from django.shortcuts import render , redirect ,HttpResponse
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout 
from django.contrib import messages 
from Xapp.models import Contact
from django.contrib.auth.decorators import login_required 
# Create your views here.
@login_required
def index(request):
    return render(request,'index.html')

def register(request): 

    if request.method == 'POST': 

        fname=request.POST.get('fname') 
        lname=request.POST.get('lname') 
        user_name=request.POST.get('uname') 
        email=request.POST.get('email') 
        password=request.POST.get('pass') 
        new_user= User.objects.create_user(user_name,email,password)
        new_user.first_name=fname
        new_user.last_name=lname
        new_user.save()
        print('Sucess')
        return redirect('loginuser')
    return render(request,'register.html')
        
def loginuser(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        login_user=authenticate(request,username=username,password=password)
        if login_user is not None:
            login(request,login_user)
            return redirect('index')
        else:
            messages.info(request,'invalid user or password')
            return redirect(loginuser)
    return render(request,'loginuser.html')

# ---------

# Create your views here.

@login_required
 
def About(request):
    return render(request,'About.html')
@login_required
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        city=request.POST.get('city')
        breed=request.POST.get('breed')
        contact = Contact(name=name, email=email, phone=phone,desc=desc,city=city,breed=breed)
        contact.save()
        messages.success(request,'message sent sucessfully')
    return render(request,'contact.html')
@login_required
def services(request):
    return render(request,'services.html')
@login_required
def sucess(request):
    return render(request,'sucess.html')
@login_required
def dog(request):
    return render(request,'dog.html')
@login_required
def cat(request):
    return render(request,'cat.html')
@login_required
def bird(request):
    return render(request,'bird.html')

def logoutuser(request): 
    logout(request) 
    return redirect('loginuser') 