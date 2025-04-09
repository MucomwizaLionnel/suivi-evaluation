from django.db import models

class ModeTransport(models.Model):
    TYPE_TRANSPORT = [
        ('bus', 'Bus'),
        ('moto', 'Moto'),
        ('velo', 'Vélo'),
        ('taxi', 'Taxi'),
        ('voiture', 'Voiture'),
    ]

    nom = models.CharField(max_length=50, choices=TYPE_TRANSPORT, unique=True)
    description = models.TextField(blank=True, null=True)
    capacite = models.IntegerField(default=1)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom


from django.db import models

class Utilisateur(models.Model):
    TYPE_UTILISATEUR = [
        ('client', 'Client'),
        ('transporteur', 'Transporteur'),
        ('administrateur', 'administrateur'),
    ]

    nom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    adresse = models.TextField(blank=True, null=True)
    type_utilisateur = models.CharField(max_length=15, choices=TYPE_UTILISATEUR)
    date_inscription = models.DateTimeField(auto_now_add=True)

    # Stocker les coordonnées GPS
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    # Uniquement pour les transporteurs
    mode_transport = models.ForeignKey(
        'ModeTransport', on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return f"{self.nom} ({self.get_type_utilisateur_display()})"

class Trajet(models.Model):
    transporteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, limit_choices_to={'type_utilisateur': 'transporteur'})
    depart = models.CharField(max_length=100)
    arrivee = models.CharField(max_length=100)
    date_depart = models.DateTimeField()
    duree_estimee = models.DurationField(blank=True, null=True)  # Durée estimée du trajet
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    places_disponibles = models.IntegerField()

    def __str__(self):
        return f"{self.depart} → {self.arrivee} ({self.transporteur.nom})"
class Reservation(models.Model):
    client = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, limit_choices_to={'type_utilisateur': 'client'})
    trajet = models.ForeignKey(Trajet, on_delete=models.CASCADE)
    date_reservation = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(
        max_length=20,
        choices=[('en attente', 'En attente'), ('confirmée', 'Confirmée'), ('annulée', 'Annulée')],
        default='en attente'
    )

    def __str__(self):
        return f"Réservation de {self.client.nom} pour {self.trajet.depart} → {self.trajet.arrivee} ({self.get_statut_display()})"
class Paiement(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    mode_paiement = models.CharField(
        max_length=20,
        choices=[('cash', 'Espèces'), ('carte', 'Carte bancaire'), ('mobile', 'Paiement mobile')]
    )
    statut = models.CharField(
        max_length=20,
        choices=[('en attente', 'En attente'), ('réussi', 'Réussi'), ('échoué', 'Échoué')],
        default='en attente'
    )
    date_paiement = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Paiement de {self.montant} € pour {self.reservation.client.nom} - {self.get_statut_display()}"
class Horaire(models.Model):
    trajet = models.ForeignKey(Trajet, on_delete=models.CASCADE)
    jour = models.CharField(
        max_length=10,
        choices=[('lundi', 'Lundi'), ('mardi', 'Mardi'), ('mercredi', 'Mercredi'), ('jeudi', 'Jeudi'), ('vendredi', 'Vendredi'), ('samedi', 'Samedi'), ('dimanche', 'Dimanche')]
    )
    heure_depart = models.TimeField()

    def __str__(self):
        return f"{self.trajet.depart} → {self.trajet.arrivee} ({self.jour} à {self.heure_depart})"
