from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login 
from superviseur.models import *
from .forms import *
from .models import *

def home(request):
    return render(request, 'home.html')





   



def loginPage(request):
    if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')
       if User.objects.filter(username=username).exists() and supervisor.objects.filter(nom=username).exists() :
        superviseur = authenticate(request, username=username, password=password)
        if superviseur:
            login(request, superviseur)
            print(username)
            return redirect('compte')
       elif client.objects.filter(nom=username).exists() and User.objects.filter(username=username).exists():
            USER = authenticate(request, username=username, password=password)
            if USER:
                login(request, USER)
                print(username)
                return redirect('home')
       else:
              return redirect('login')
    return render(request, 'login.html')