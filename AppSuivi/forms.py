from django import forms
from .models import *

class RecetteForm(forms.ModelForm):
    class Meta:
        model = Recette
        fields = ['projet', 'montant', 'description', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class DepenseForm(forms.ModelForm):
    class Meta:
        model = Recette
        fields = ['projet', 'montant', 'description', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class ProjetForm(forms.ModelForm):
    class Meta:
        model = Projet
        fields = ['nom','description','budget_prevu','date_debut','date_fin','statut']

        widgets = {
            'date_debut': forms.DateInput(attrs={'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

