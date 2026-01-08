from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("doctors_list")  
    else: 
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("doctors_list") 

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You succesfuly loged in")
            return redirect("doctors_list") 
        else:
            messages.errors(request,"Wrong name or password")
    return render(request, "accounts/login.html")

        