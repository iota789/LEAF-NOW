
from inspect import formatargvalues
from django.shortcuts import  render, redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django import forms
from .forms import CUserCreationForm,donator

from calc.forms import CUserCreationForm, donator
# Create your views here.
def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'home.html')
def donate(request):
    return render(request,'donate.html')
def aboutus(request):
    return render(request,'aboutus.html')
def buy(request):
    return render(request,'buy.html')
def disc(request):
    return render(request,'discussion.html')
def login1(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
             return render(request,'login.html')                  
    context={}
    return render(request,'login.html',context)
def plants(request):
    return render(request,'plants.html')
def seeds(request):
    return render(request,'seeds.html')
def sell(request):
    return render(request,'sell.html')    
def cart(request):
    return render(request,'cart.html')
def fm1(request):
    form=donator()
    if request.method == 'POST':
        form = donator(request.POST)
        if form.is_valid():
            form.save()
            return redirect('yay')
    context={
        'form':form
        }
    return render(request,'form1.html',context)
def fm2(request):
    form=donator()
    if request.method == 'POST':
        form = donator(request.POST)
        if form.is_valid():
            form.save()
            return redirect('yay')
    context={
        'form':form
        }
    return render(request,'form2.html',context)
def signup(request):
    form=CUserCreationForm()
    if request.method=='POST':
        form=CUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login1')
    context={'form':form}
    return render (request,'signup.html',context)     
def logout1(request):
    logout(request)
    return redirect('login1')
def yay(request):
    return render(request,'yay.html')
