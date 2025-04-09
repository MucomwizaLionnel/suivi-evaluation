from django.shortcuts import render,redirect

from .models import *
from .forms import *  # Assurez-vous d'avoir un formulaire pour la Recette

def ajouter_recette(request):
    if request.method == "POST":
        form = RecetteForm(request.POST.copy())
        if form.is_valid():
            projet = form.cleaned_data['projet']
            montant = form.cleaned_data['montant']
            description = form.cleaned_data['description']
            date = form.cleaned_data['date']
            
            # Vérifie si une recette identique existe déjà
            if not Recette.objects.filter(projet=projet, montant=montant, description=description, date=date).exists():
                form.save()
                return redirect('recette')  # Évite la soumission multiple
            else:
                form.add_error(None, "Cette recette existe déjà.")

    else:
        form = RecetteForm()

    return render(request, 'ajouter_recette.html', {'form': form})


def recette(request):
    
    recettes = Recette.objects.all() 

    return render(request, 'recette.html',{'recettes':recettes})   
