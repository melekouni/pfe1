from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login 


@login_required
def dashbord(request):
    return render(request, 'admin.html')





   



