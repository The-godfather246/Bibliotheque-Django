from django.db import models
from django.utils import timezone

class Livre(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    categorie = models.CharField(max_length=100)
    quantite_totale = models.IntegerField()
    quantite_disponible = models.IntegerField()

    def __str__(self):
        return self.titre

class Membre(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=15)
    date_inscription = models.DateField(auto_now_add=True)
    abonnement = models.ForeignKey('Abonnement', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Abonnement(models.Model):
    TYPE_CHOICES = [
        ('mensuel', 'Mensuel'),
        ('trimestriel', 'Trimestriel'),
        ('annuel', 'Annuel'),
    ]
    type = models.CharField(max_length=11, choices=TYPE_CHOICES)
    duree = models.IntegerField()  # en jours
    cout = models.DecimalField(max_digits=10, decimal_places=2)
    nombre_max_livres = models.IntegerField()
    date_renouvellement = models.DateField(null=True, blank=True)  # Ajoutez ce champ
    date_expiration = models.DateField(null=True, blank=True)  # Ajoutez ce champ

    def __str__(self):
        return f"{self.get_type_display()} ({self.duree} jours, {self.cout} €)"

class Emprunt(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)
    date_emprunt = models.DateField(auto_now_add=True)
    date_retour_prevue = models.DateField()
    STATUS_CHOICES = [
        ('en cours', 'En cours'),
        ('retourné', 'Retourné'),
        ('en retard', 'En retard'),
    ]
    statut = models.CharField(max_length=20, choices=STATUS_CHOICES, default='en cours')

    def est_en_retard(self):
        return self.date_retour_prevue < timezone.now().date() and self.statut == 'en cours'

    def __str__(self):
        return f"{self.livre.titre} emprunté par {self.membre.nom} {self.membre.prenom}"
