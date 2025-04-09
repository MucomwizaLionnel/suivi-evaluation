from django.urls import path
from . import views
from .viewstab import tableau
from .viewsrecette import ajouter_recette,recette
from .viewsdepense import ajouter_depense,depense
from .viewsdetaillprojet import detail_projet
from .viewspersonnel import listepersonnel
from .viewspaiement import liste_paiement
urlpatterns = [
    path('', tableau, name='tableau'),
    path('dash/', views.dashboard, name='dashboard'),
    path('evaluer/<int:projet_id>/', views.evaluer_projet, name='evaluer_projet'),
    path('ajouter-recette/', ajouter_recette, name='ajouter_recette'),
    path('afficherecette/', recette, name='recette'),
    path('ajouter_depense/', ajouter_depense,name='ajouter_depense'),
    path('affichedepense/', depense,name='depense'),
    path('detailprojet/<int:id>/', detail_projet,name='detailprojet'),
    path('listepersonnel/', listepersonnel,name='listepersonnel'),
    path('liste_paiement/', liste_paiement,name='liste_paiement'),

]
