from django.contrib import admin
from .models import Livre, Membre, Abonnement, Emprunt

admin.site.register(Livre)
admin.site.register(Membre)
admin.site.register(Abonnement)
admin.site.register(Emprunt)
