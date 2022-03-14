from asyncio.windows_events import NULL
from enum import auto
from typing_extensions import Self
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User, Group

from numpy import True_
# Create your models here.

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

class Lead(models.Model):
    id=models.IntegerField(auto, primary_key=True)
    Name=models.CharField("Full Name",max_length=30)
    email=models.EmailField(max_length=50)
    phone_number=models.IntegerField()
    created_at=models.DateTimeField("date_created",default=datetime.now())
    Status=models.CharField(max_length = 50, choices=[('hot','hot'),('cold','cold'),('med','med'),('sold','sold')])
    user_id=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Assigned to")
    
    def __str__(self) -> str: 
        return self.Name
