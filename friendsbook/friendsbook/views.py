from django.shortcuts import render
from django.contrib.auth.models import User

def Home(request):
    user=request.user
    return render(request,'main/home.html',{"user":user})