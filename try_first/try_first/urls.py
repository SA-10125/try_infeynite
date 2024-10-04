"""
URL configuration for try_first project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
]
#essentially, i want to store the images in the db (maybe as strings using base64) we will use a default image and store a new message in each reupload of that image. 
#the making image part is his deal, you need to store em, just like events stuff, make sure each one gets which they need to get and none else and figure out how you will encrypt it end to end.
#for the e2e enc, use encrypt ideas.
#let me get started with login page first, once login works, i can start with sharing and how to go about that, we want gmail vibes, one page to compose message and lets see idk
#also figure out how to use AES