from django.shortcuts import render,redirect

from .models import *
from .forms import *  # Assurez-vous d'avoir un formulaire pour la Recette

def ajouter_depense(request):
    if request.method == "POST":
        form = DepenseForm(request.POST.copy())
        if form.is_valid():
            projet = form.cleaned_data['projet']
            montant = form.cleaned_data['montant']
            description = form.cleaned_data['description']
            date = form.cleaned_data['date']
            
            # Vérifie si une recette identique existe déjà
            if not Depense.objects.filter(projet=projet, montant=montant, description=description, date=date).exists():
                form.save()
                return redirect('depense')  # Évite la soumission multiple
            else:
                form.add_error(None, "Cette recette existe déjà.")

    else:
        form = DepenseForm()

    return render(request, 'ajouter_depense.html', {'form': form})


def depense(request):
    
    depenses = Depense.objects.all() 

    return render(request, 'depense.html',{'depenses':depenses})   
