from django.shortcuts import render,redirect

from .models import *

def tableau(request):

    return render(request,'tableau.html')