from django.db import models
from datetime import datetime
# Create your models here.

class SiteUser(models.Model):
    First_name=models.CharField(max_length=30)
    Last_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    phone_number=models.IntegerField()
    password=models.CharField(max_length=30)
    created_at=models.DateTimeField("date_created",default=datetime.now())

    def __str__(self) -> str: 
        return self.First_name
