from django import forms
from .models import Livre, Membre, Abonnement, Emprunt

class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = '__all__'

class MembreForm(forms.ModelForm):
    class Meta:
        model = Membre
        fields = '__all__'

class AbonnementForm(forms.ModelForm):
    class Meta:
        model = Abonnement
        fields = '__all__'

class EmpruntForm(forms.ModelForm):
    class Meta:
        model = Emprunt
        fields = '__all__'
