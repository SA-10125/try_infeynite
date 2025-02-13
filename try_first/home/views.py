import datetime
from django.forms import DateTimeField
from django.shortcuts import render, redirect
from django.contrib import messages #this is what we import to get flash messages.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout #imported for the user login
from django.contrib.auth.decorators import login_required,user_passes_test #this is used to restrict pages that need login or a certain login.
from django.utils import timezone
from .models import *
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import SignUpForm
from .models import IDCard


#empty = login page (home) #redirects to messages page (test)
#home/ = first page (first) #add signup button and signup function
#logout/ = logs out user adn redirects to first page (logout)
#admin/ = admin

# Create your views here.
def loginPage(request):
    if request.user.is_authenticated:
        return(redirect('events'))#test
    if request.method=="POST":
        username=request.POST.get('Fusn')#user.username
        password=request.POST.get('Fpwd')
        email=request.POST.get('email') #figure out how to take this during signup
        try: #when one person first messages someone else, create a one to one relationship between them like a linkage and have the messages go via that linkage?
            
            user=User.objects.get(username=username)
        except:
            messages.error(request,'Username does not exist. Please sign up instead.') #add signup button to this page that redirects to signup page. 
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return(redirect('events'))#test
        else:
            messages.error(request,"Username and password don't match.")
    
    context={}
    return(render(request,'login.html',context))

@login_required(login_url='home') #just in case.
def logoutPage(request):#removed GI stuff
    logout(request) 
    return(redirect('home'))

def helloworld(request):
    return(render(request,'firsthack.html'))

def signuppage(request):
    try:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)  # Log the user in after signup
                messages.success(request, 'Signup successful!')
                return redirect('IDmake')  # Redirect to a home page or another view
        else:
            form = SignUpForm()
        context = {'form': form}
        return render(request, 'signup.html', context)
    except:
        return(redirect('IDmake'))

def idmakepage(request):
    try:
        IDCard.objects.get(user=request.user)
    except: #if user doesnt have an id after sign up
        if request.method=="POST":
            myID=request.POST.get('Fuid')
            try: 
                test=IDCard.objects.get(UserID=myID)
                messages.error(request,'User ID taken, try again.')
            except:
                ID=IDCard.objects.create(user=request.user,UserID=myID)
                return(redirect('home'))
        else:
            return(render(request,'cardpage.html'))
    return(redirect('events'))#test