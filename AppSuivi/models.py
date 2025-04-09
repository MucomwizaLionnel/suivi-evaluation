from django.db import models
from django.contrib.auth.models import User



class Personnel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fonction = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    salaire = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.user


class Projet(models.Model):
    STATUT_CHOICES = [
        ('En cours', 'En cours'),
        ('Terminé', 'Terminé'),
        ('Évalué', 'Évalué')
    ]

    nom = models.CharField(max_length=100)
    description = models.TextField()
    budget_prevu = models.DecimalField(max_digits=12, decimal_places=2)
    date_debut = models.DateField()
    date_fin = models.DateField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='En cours')
    responsable = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nom

class Activite(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    titre = models.CharField(max_length=255)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    responsable = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    statut = models.CharField(max_length=20, choices=[('Prévue', 'Prévue'), ('En cours', 'En cours'), ('Terminée', 'Terminée')])

    def __str__(self):
        return f"{self.titre} - {self.projet.titre}"


class Indicateur(models.Model):
    activite = models.ForeignKey(Activite, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    unite = models.CharField(max_length=50)
    valeur_cible = models.DecimalField(max_digits=10, decimal_places=2)
    valeur_atteinte = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_mesure = models.DateField()

    def __str__(self):
        return f"{self.nom} ({self.activite.titre})"


class Depense(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    date = models.DateField()

class Recette(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    date = models.DateField()

class Realisation(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    description = models.TextField()
    taux_execution = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()

class Evaluation(models.Model):
    DECISION_CHOICES = [
        ('Rentable', 'Rentable'),
        ('Non rentable', 'Non rentable')
    ]

    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    resultat_net = models.DecimalField(max_digits=12, decimal_places=2)
    taux_rentabilite = models.DecimalField(max_digits=5, decimal_places=2)
    decision = models.CharField(max_length=20, choices=DECISION_CHOICES)
    date_evaluation = models.DateField(auto_now_add=True)

class RapportSuivi(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    date = models.DateField()
    resume_activites = models.TextField()
    avancement = models.TextField()
    difficultes = models.TextField()
    recommandations = models.TextField()

    def __str__(self):
        return f"Rapport - {self.projet.titre} - {self.date}"

class Justificatif(models.Model):
    depense = models.ForeignKey(Depense, on_delete=models.CASCADE)
    fichier = models.FileField(upload_to='justificatifs/')
    date_ajout = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Justificatif - {self.depense.description[:30]}"
class CommentaireEvaluation(models.Model):
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    auteur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    commentaire = models.TextField()
    date_commentaire = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire par {self.auteur} le {self.date_commentaire.strftime('%d/%m/%Y')}"

class AffectationPersonnel(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.personnel} affecté à {self.projet}"
