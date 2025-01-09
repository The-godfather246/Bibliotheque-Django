from django.urls import path
from . import views

urlpatterns = [
    
    # URLs pour les livres
    path('livres/', views.liste_livres, name='liste_livres'),
    path('livres/ajouter/', views.ajouter_livre, name='ajouter_livre'),
    path('livres/modifier/<int:pk>/', views.modifier_livre, name='modifier_livre'),
    path('livres/supprimer/<int:pk>/', views.supprimer_livre, name='supprimer_livre'),

    # URLs pour les membres
    path('membres/', views.liste_membres, name='liste_membres'),
    path('membres/ajouter/', views.ajouter_membre, name='ajouter_membre'),
    path('membres/modifier/<int:pk>/', views.modifier_membre, name='modifier_membre'),
    path('membres/supprimer/<int:pk>/', views.supprimer_membre, name='supprimer_membre'),

    # URLs pour les abonnements
    path('abonnements/', views.liste_abonnements, name='liste_abonnements'),
    path('abonnements/ajouter/', views.ajouter_abonnement, name='ajouter_abonnement'),
    path('abonnements/modifier/<int:pk>/', views.modifier_abonnement, name='modifier_abonnement'),
    path('abonnements/supprimer/<int:pk>/', views.supprimer_abonnement, name='supprimer_abonnement'),

    # URLs pour les emprunts
    path('emprunts/', views.liste_emprunts, name='liste_emprunts'),
    path('emprunts/ajouter/', views.ajouter_emprunt, name='ajouter_emprunt'),
    path('emprunts/modifier/<int:pk>/', views.modifier_emprunt, name='modifier_emprunt'),
    path('emprunts/supprimer/<int:pk>/', views.supprimer_emprunt, name='supprimer_emprunt'),

    # URL pour la recherche de livres
    path('recherche/', views.recherche_livres, name='recherche_livres'),

    # URL pour le tableau de bord
    path('tableau_de_bord/', views.tableau_de_bord, name='tableau_de_bord'),

    # URL pour les rapports
    path('rapports/', views.rapports, name='rapports'),
]
