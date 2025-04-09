from django.shortcuts import render,redirect,get_object_or_404

from .models import *

from django.db.models import Sum


def detail_projet(request, id):
    projet = get_object_or_404(Projet, id=id)

    total_recettes = Recette.objects.filter(projet=projet).aggregate(total=Sum('montant'))['total'] or 0
    total_depenses = Depense.objects.filter(projet=projet).aggregate(total=Sum('montant'))['total'] or 0

    # Trouver tous les personnels affectés à ce projet
    affectations = AffectationPersonnel.objects.filter(projet=projet)
    personnels = affectations.values_list('personnel', flat=True)

    # Calcul des paiements pour ces personnels
    total_salaires = Paiement.objects.filter(personnel__in=personnels).aggregate(total=Sum('montant'))['total'] or 0

    solde_net = total_recettes - (total_depenses + total_salaires)

    context = {
        'projet': projet,
        'total_recettes': total_recettes,
        'total_depenses': total_depenses,
        'total_salaires': total_salaires,
        'solde_net': solde_net,
    }

    return render(request, 'detail_projet.html', context)
