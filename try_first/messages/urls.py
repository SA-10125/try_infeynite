from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.displaymessages,name='events'),
    path('view/<str:pk>/',views.messageshow,name='msgview'),
    path('compose/',views.compose,name='compose'),
]