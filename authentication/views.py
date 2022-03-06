from django.shortcuts import render, HttpResponse, redirect
from authentication.models import SiteUser
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from .forms import registration

# Create your views here.
def index(request):
    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        # print(request.POST.get('first_name'))
        # form = registration(request.POST)
            # user=SiteUser(First_name=request.POST.get('first_name'),)
            # user.save()
        # if form.is_valid():
        #     form.save()
        
        First_name=request.POST.get('first_name')
        Last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        phone_number=request.POST.get('phone_number')
        password=request.POST.get('password')
        SiteUser.objects.create(First_name=First_name, Last_name=Last_name, email=email, phone_number=phone_number )
        redirect("/login")
        
    return render(request, "register.html") 