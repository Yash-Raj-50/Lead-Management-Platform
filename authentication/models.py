# from asyncio.windows_events import NULL
from enum import auto
from typing_extensions import Self
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User, Group
from numpy import True_
from django.shortcuts import get_object_or_404

###
Default_fk_id=1
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Manager_is=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Manage_id", related_name='Manager',default=Default_fk_id)
    avatar = models.ImageField(upload_to='', default='profile.png')

    def __str__(self):
        return self.user.username

class LeadManager(models.Manager):
    def get_queryset(self,request): 
        query= Lead.objects.filter(user_id=request.user)
        if request.user.is_superuser:
            query = Lead.objects.all()
        if request.user in User.objects.filter(groups__name__in=['Manager']):
            # query = Lead.objects.filter(user_id= any(User.objects.filter( Manager=request.user.user_id)))
            query = Lead.objects.all()
        return query

class Lead(models.Model):
    id=models.AutoField( primary_key=True)
    Name=models.CharField("Full Name",max_length=30)
    email=models.EmailField(max_length=50)
    phone_number=models.IntegerField()
    created_at=models.DateTimeField("date_created",default=datetime.now())
    Status=models.CharField(max_length = 50, choices=[('hot','hot'),('cold','cold'),('med','med'),('sold','sold')])
    user_id=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Assigned to")
    remark = models.TextField(default="Add+")
    remarks_data=models.TextField(null=True)
    def __str__(self) -> str: 
        return self.Name

class SiteUser(models.Model):
    id=models.IntegerField(auto, primary_key=True)
    First_name=models.CharField(max_length=30)
    Last_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    phone_number=models.IntegerField()
    password=models.CharField(max_length=30)
    created_at=models.DateTimeField("date_created",default=datetime.now())
    is_approved=models.BooleanField(default=False)

    def __str__(self) -> str: 
        return self.First_name

