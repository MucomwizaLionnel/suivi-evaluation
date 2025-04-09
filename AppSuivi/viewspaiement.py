from django.shortcuts import render,redirect

from .models import *

def liste_paiement(request):
    paiements= Paiement.objects.all()

    return render(request,'paiement.html' ,{'paiements': paiements} ) 