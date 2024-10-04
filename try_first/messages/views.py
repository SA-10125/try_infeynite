import datetime
from django.db.models import Q
from django.forms import DateTimeField
from django.shortcuts import render, redirect
from django.contrib import messages #this is what we import to get flash messages.
from django.contrib.auth.models import User
from home.models import IDCard,message,pouchoftwo
from django.contrib.auth import authenticate,login,logout #imported for the user login
from django.contrib.auth.decorators import login_required,user_passes_test #this is used to restrict pages that need login or a certain login.
from django.utils import timezone
from .crypt import create_keypair, encode, decode
import string
import random

# Create your views here.
#empty = hi2.html (shows all the messages as buttons then uses pk to show each message)

@login_required(login_url='home') #might change login url
def displaymessages(request): #ADD A COMPOSE BUTTON (but dotn call it compose)
    context={}
    try:
        mymessages=message.objects.all() #if there are messages to go through.
    except:
        mymessages=[] #if there are no messages to go through.
    myID=IDCard.objects.get(user=request.user)
    mymessages=[i for i in mymessages if i.Reciever==myID.UserID] #encrypted messages but subject is seen.
    context['messages']=mymessages #define my messages as any messages to which you are reciver.
    #have messages be objects with sender id and reciever id and the picture somehow (preferably as text provided he can take it out)
    return(render(request,'messagedisplay.html',context))

def messageshow(request,pk):
    context={}
    msg=message.objects.get(msgID=pk)
    myID=IDCard.objects.get(user=request.user)
    try:
        keysthing = pouchoftwo.objects.filter(Q(ID1=msg.Sender, ID2=msg.Reciever) | Q(ID1=msg.Reciever, ID2=msg.Sender))[0]

    except IndexError:
        secret,public=create_keypair()
        keysthing=pouchoftwo.objects.create(ID1=message.Sender, ID2=message.Reciever, PrivateKey=secret, PublicKey=public)

    msg.Message=decode(msg.Message, keysthing.PrivateKey)
    context['msg']=msg
    #if msg.Reciever!=myID:
    #    return(redirect('logout'))
    return(render(request,'messagesee.html',context))
    
def compose(request):
    if request.method=="POST":
        whomto=request.POST.get('Fto')
        sub=request.POST.get('Fsub')
        msg=request.POST.get('Fmsg')

        myID=IDCard.objects.get(user=request.user)
        try:
            keysthing = pouchoftwo.objects.filter(Q(ID1=myID, ID2=whomto) | Q(ID1=whomto, ID2=myID))[0]

        except IndexError:
            secret,public=create_keypair()
            keysthing=pouchoftwo.objects.create(ID1=myID, ID2=whomto, PrivateKey=secret, PublicKey=public)

        # using random.choices() generating random strings
        ID = f'{sub}'.join(random.choices(string.ascii_letters,k=7)) # initializing size of string

        msg=encode(msg, keysthing.PublicKey)
        mymsg=message.objects.create(Sender=myID,Reciever=whomto,Subject=sub,Message=msg,msgID=ID)

    context={}
    return(render(request,'compose.html'))