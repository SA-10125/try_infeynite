from django.db import models as m
from django.contrib.auth.models import User

class IDCard(m.Model): # FYI: It has all the attributes of User such as .is_authenticated etc... since it has inherited from User via onetoone
    user = m.OneToOneField(User, on_delete=m.CASCADE,related_name='me')# this is just to make a onetoone connection between a user and this.
    UserID = m.CharField(max_length=500,null=False,blank=False)
    def __str__(self):
        return f"{self.user.username}-{self.UserID}"

class pouchoftwo(m.Model):
    ID1=m.CharField(max_length=500,null=False,blank=False)
    ID2=m.CharField(max_length=500,null=False,blank=False)
    PrivateKey=m.CharField(max_length=500,null=False,blank=False)
    PublicKey=m.CharField(max_length=500,null=False,blank=False)
    def __str__(self):
        return f"{self.ID1}-{self.ID2}"
    class Meta:
        unique_together=[['ID1','ID2']]

class message(m.Model):
    Sender=m.CharField(max_length=500,null=False,blank=False)
    Reciever=m.CharField(max_length=500,null=False,blank=False)
    Subject=m.CharField(max_length=500,null=True,blank=True)
    Message=m.CharField(max_length=15000,null=False,blank=False)
    msgID=m.CharField(max_length=500,null=False,blank=False)
    date=m.DateTimeField

    def __str__(self):
        return f"{self.Sender}-{self.Reciever}-{self.msgID}"
    class Meta:
        unique_together=[['msgID']]


