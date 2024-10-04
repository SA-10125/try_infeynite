from django.urls import path,include
from . import views

urlpatterns=[
    path('home/',views.helloworld,name='first'),#homepage
    path('',views.loginPage,name='home'),#login
    path('logout/',views.logoutPage,name='logout'),
    path('mesages/',include('messages.urls')),
    path('signup/',views.signuppage,name='signup'),
    path('idmake/',views.idmakepage,name='IDmake'),
    
    #events.html basically
]