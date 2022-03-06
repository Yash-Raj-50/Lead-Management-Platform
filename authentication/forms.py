from django import forms
from datetime import datetime

class registration(forms.Form):
    First_name=forms.CharField(max_length=30)
    Last_name=forms.CharField(max_length=30)
    email=forms.EmailField(max_length=50)
    phone_number=forms.IntegerField()
    password=forms.CharField(max_length=30)
    # created_at=forms.DateTimeField("date_created",default=datetime.now())