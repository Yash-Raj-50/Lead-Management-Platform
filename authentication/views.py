from enum import auto
from django.shortcuts import render, HttpResponse, redirect
from authentication.models import Lead, SiteUser
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from .forms import registration
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from django.contrib.auth.models import User, Permission, Group
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count

# Create your views here.
def index(request):
    return render(request, "login.html")

def signin(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')

        username = User.objects.get(email=email).username

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            if user.groups.filter(name='Representative'):
                return redirect('/admin/authentication/lead')
            else:
                return redirect('/admin')
        else:
            messages.error(request, "Incorrect Email or Password")
            return redirect('/login')
    

def register(request):
    if request.method == "POST":
        # print(request.POST.get('first_name'))
        # form = registration(request.POST)
            # user=SiteUser(First_name=request.POST.get('first_name'),)
            # user.save()
        # if form.is_valid():
        #     form.save()
        id= auto
        # print(id)
        First_name=request.POST.get('first_name')
        Last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        # phone_number=request.POST.get('phone_number')
        password=request.POST.get('password')
        
        name=First_name+Last_name
        user=User.objects.create_user(username=name, email=email, password=password, is_staff=False)
        user.set_password(password)
        user.first_name= First_name
        user.last_name= Last_name
        my_group = Group.objects.get(name='Representative') 
        my_group.user_set.add(user)
        user.save()

        return redirect("/login")
        
    return render(request, "register.html") 

def error_404_view(request, exception):
    return render(request,'error_404.html')

def logout_request(request):
    logout(request)
    return redirect("/login")

def dashboard(request):
    leads=Lead.objects.all()
    context={
        'leads' : leads,
    }
    return render(request,'dashboard.html', context)

user= get_user_model()

class chartData(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        statusdata =  list(Lead.objects.values_list("Status", flat=True))

        labels=['cold','hot','med','sold']
        default_items=[statusdata.count('cold'),
                        statusdata.count('hot'),
                        statusdata.count('med'),
                        statusdata.count('sold'),
                    ]
        
        data ={
            "labels": labels,
            "default": default_items,
            "no_total": sum(default_items),

        }
        return Response(data)