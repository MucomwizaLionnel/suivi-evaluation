from django.shortcuts import render,redirect

from .models import *
from .forms import *  # Assurez-vous d'avoir un formulaire pour la Recette

def ajouter_projet(request):
    if request.method == "POST":
        form = ProjetForm(request.POST.copy())
        if form.is_valid():
            nom = form.cleaned_data['nom']
            
            description = form.cleaned_data['description']
            budget_prevu = form.cleaned_data['budget_prevu']
            date_debut = form.cleaned_data['date_debut']
            date_fin = form.cleaned_data['date_fin']
            statut=form.cleaned_data['statut']
            
            # Vérifie si une recette identique existe déjà
            if not Projet.objects.filter( nom= nom, budget_prevu=budget_prevu, description=description, date_debut=date_debut,date_fin=date_fin,statut=statut).exists():
                form.save()
                return redirect('dashboard')  # Évite la soumission multiple
            else:
                form.add_error(None, "Cette projet existe déjà.")

    else:
        form = ProjetForm()

    return render(request, 'ajouter_projet.html', {'form': form})



