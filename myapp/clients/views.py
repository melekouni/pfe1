from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate , login 



def dashbord(request):
    return render(request, 'admin.html')
