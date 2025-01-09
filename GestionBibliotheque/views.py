from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Livre, Membre, Abonnement, Emprunt
from .forms import LivreForm, MembreForm, AbonnementForm, EmpruntForm
from django.utils import timezone 
# Vues pour les livres
def liste_livres(request):
    livres = Livre.objects.all()
    return render(request, 'gestion_bibliotheque/liste_livres.html', {'livres': livres})

def ajouter_livre(request):
    if request.method == 'POST':
        form = LivreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_livres')
    else:
        form = LivreForm()
    return render(request, 'gestion_bibliotheque/ajouter_livre.html', {'form': form})

def modifier_livre(request, pk):
    livre = get_object_or_404(Livre, pk=pk)
    if request.method == 'POST':
        form = LivreForm(request.POST, instance=livre)
        if form.is_valid():
            form.save()
            return redirect('liste_livres')
    else:
        form = LivreForm(instance=livre)
    return render(request, 'gestion_bibliotheque/modifier_livre.html', {'form': form})

def supprimer_livre(request, pk):
    livre = get_object_or_404(Livre, pk=pk)
    if request.method == 'POST':
        livre.delete()
        return redirect('liste_livres')
    return render(request, 'gestion_bibliotheque/supprimer_livre.html', {'livre': livre})

# Vues pour les membres
def liste_membres(request):
    membres = Membre.objects.all()
    return render(request, 'gestion_bibliotheque/liste_membres.html', {'membres': membres})

def ajouter_membre(request):
    if request.method == 'POST':
        form = MembreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_membres')
    else:
        form = MembreForm()
    return render(request, 'gestion_bibliotheque/ajouter_membre.html', {'form': form})

def modifier_membre(request, pk):
    membre = get_object_or_404(Membre, pk=pk)
    if request.method == 'POST':
        form = MembreForm(request.POST, instance=membre)
        if form.is_valid():
            form.save()
            return redirect('liste_membres')
    else:
        form = MembreForm(instance=membre)
    return render(request, 'gestion_bibliotheque/modifier_membre.html', {'form': form})

def supprimer_membre(request, pk):
    membre = get_object_or_404(Membre, pk=pk)
    if request.method == 'POST':
        membre.delete()
        return redirect('liste_membres')
    return render(request, 'gestion_bibliotheque/supprimer_membre.html', {'membre': membre})

# Vues pour les abonnements
def liste_abonnements(request):
    abonnements = Abonnement.objects.all()
    return render(request, 'gestion_bibliotheque/liste_abonnements.html', {'abonnements': abonnements})

def ajouter_abonnement(request):
    if request.method == 'POST':
        form = AbonnementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_abonnements')
    else:
        form = AbonnementForm()
    return render(request, 'gestion_bibliotheque/ajouter_abonnement.html', {'form': form})

def modifier_abonnement(request, pk):
    abonnement = get_object_or_404(Abonnement, pk=pk)
    if request.method == 'POST':
        form = AbonnementForm(request.POST, instance=abonnement)
        if form.is_valid():
            form.save()
            return redirect('liste_abonnements')
    else:
        form = AbonnementForm(instance=abonnement)
    return render(request, 'gestion_bibliotheque/modifier_abonnement.html', {'form': form})

def supprimer_abonnement(request, pk):
    abonnement = get_object_or_404(Abonnement, pk=pk)
    if request.method == 'POST':
        abonnement.delete()
        return redirect('liste_abonnements')
    return render(request, 'gestion_bibliotheque/supprimer_abonnement.html', {'abonnement': abonnement})

# Vues pour les emprunts
def liste_emprunts(request):
    emprunts = Emprunt.objects.all()
    return render(request, 'gestion_bibliotheque/liste_emprunts.html', {'emprunts': emprunts})

def ajouter_emprunt(request):
    if request.method == 'POST':
        form = EmpruntForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_emprunts')
    else:
        form = EmpruntForm()
    return render(request, 'gestion_bibliotheque/ajouter_emprunt.html', {'form': form})

def modifier_emprunt(request, pk):
    emprunt = get_object_or_404(Emprunt, pk=pk)
    if request.method == 'POST':
        form = EmpruntForm(request.POST, instance=emprunt)
        if form.is_valid():
            form.save()
            return redirect('liste_emprunts')
    else:
        form = EmpruntForm(instance=emprunt)
    return render(request, 'gestion_bibliotheque/modifier_emprunt.html', {'form': form})

def supprimer_emprunt(request, pk):
    emprunt = get_object_or_404(Emprunt, pk=pk)
    if request.method == 'POST':
        emprunt.delete()
        return redirect('liste_emprunts')
    return render(request, 'gestion_bibliotheque/supprimer_emprunt.html', {'emprunt': emprunt})

# Vue pour la recherche de livres
def recherche_livres(request):
    query = request.GET.get('q')
    if query:
        livres = Livre.objects.filter(titre__icontains=query) | Livre.objects.filter(auteur__icontains=query) | Livre.objects.filter(categorie__icontains=query) | Livre.objects.filter(isbn__icontains=query)
    else:
        livres = Livre.objects.none()
    return render(request, 'gestion_bibliotheque/recherche_livres.html', {'livres': livres})

from django.shortcuts import render
from .models import Livre, Membre, Abonnement, Emprunt
from django.utils import timezone

def tableau_de_bord(request):
    total_livres = Livre.objects.count()
    abonnements_actifs = Membre.objects.filter(abonnement__isnull=False).count()
    livres_empruntes = Emprunt.objects.filter(statut='en cours').count()
    retours_en_attente = Emprunt.objects.filter(statut='en retard').count()
    membres_actifs = Membre.objects.filter(abonnement__isnull=False).count()
    membres_inactifs = Membre.objects.filter(abonnement__isnull=True).count()

    statistiques_emprunts = Emprunt.objects.filter(date_emprunt__month=timezone.now().month)
    abonnements_renouveles = Abonnement.objects.filter(date_renouvellement__month=timezone.now().month)
    abonnements_expirés = Abonnement.objects.filter(date_expiration__month=timezone.now().month)

    return render(request, 'gestion_bibliotheque/tableau_de_bord.html', {
        'total_livres': total_livres,
        'abonnements_actifs': abonnements_actifs,
        'livres_empruntes': livres_empruntes,
        'retours_en_attente': retours_en_attente,
        'membres_actifs': membres_actifs,
        'membres_inactifs': membres_inactifs,
        'statistiques_emprunts': statistiques_emprunts,
        'abonnements_renouveles': abonnements_renouveles,
        'abonnements_expirés': abonnements_expirés,
    })


# Vue pour les rapports
def rapports(request):
    statistiques_emprunts = Emprunt.objects.filter(date_emprunt__month=timezone.now().month)
    abonnements_renouveles = Abonnement.objects.filter(date_renouvellement__month=timezone.now().month)
    abonnements_expirés = Abonnement.objects.filter(date_expiration__month=timezone.now().month)
    return render(request, 'gestion_bibliotheque/rapports.html', {
        'statistiques_emprunts': statistiques_emprunts,
        'abonnements_renouveles': abonnements_renouveles,
        'abonnements_expirés': abonnements_expirés,
    })
