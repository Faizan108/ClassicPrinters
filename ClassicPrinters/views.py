from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import login as dj_login,logout as dj_logout,authenticate
from django.contrib import messages


def home(request):
    return render(request, 'home.html')