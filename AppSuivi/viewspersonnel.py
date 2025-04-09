from django.shortcuts import render,redirect

from .models import *

def listepersonnel(request):
    personnels=Personnel.objects.all()
   
    return render(request,'liste_personnel.html',{'personnels' : personnels}  )