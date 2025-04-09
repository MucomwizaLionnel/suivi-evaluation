from django.shortcuts import render,redirect

from .models import *
def dashboard(request):
    
    projets = Projet.objects.all()
    data = []

    for projet in projets:
        total_depenses = sum(d.montant for d in projet.depense_set.all())
        total_recettes = sum(r.montant for r in projet.recette_set.all())

        affectations = AffectationPersonnel.objects.filter(projet=projet).select_related('personnel')
        total_salaires = sum(a.personnel.salaire for a in affectations)
        
        resultat = total_recettes - (total_depenses+total_salaires)
        evaluation = Evaluation.objects.filter(projet=projet).last()
        rentabilite = evaluation.decision if evaluation else "Non évalué"

        data.append({
            'projet': projet,
            'depenses': total_depenses,
            'recettes': total_recettes,
            'resultat': resultat,
            'salaires':total_salaires,
            'rentabilite': rentabilite
        })

    return render(request, 'dashboard.html', {'data': data})

def evaluer_projet(request, projet_id):
    projet = Projet.objects.get(id=projet_id)
    total_depenses = sum(d.montant for d in projet.depense_set.all())
    total_recettes = sum(r.montant for r in projet.recette_set.all())
    resultat_net = total_recettes - total_depenses
    taux = (resultat_net / projet.budget_prevu) * 100 if projet.budget_prevu else 0
    decision = "Rentable" if resultat_net >= 0 else "Non rentable"

    Evaluation.objects.create(
        projet=projet,
        resultat_net=resultat_net,
        taux_rentabilite=taux,
        decision=decision
    )
    return redirect('dashboard')

def tableau(request):
    return render(request='tableaau.html')
