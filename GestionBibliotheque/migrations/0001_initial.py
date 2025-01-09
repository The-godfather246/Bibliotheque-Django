# Generated by Django 5.1.4 on 2025-01-09 14:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abonnement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('mensuel', 'Mensuel'), ('trimestriel', 'Trimestriel'), ('annuel', 'Annuel')], max_length=11)),
                ('duree', models.IntegerField()),
                ('cout', models.DecimalField(decimal_places=2, max_digits=10)),
                ('nombre_max_livres', models.IntegerField()),
                ('date_renouvellement', models.DateField(blank=True, null=True)),
                ('date_expiration', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('auteur', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('categorie', models.CharField(max_length=100)),
                ('quantite_totale', models.IntegerField()),
                ('quantite_disponible', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telephone', models.CharField(max_length=15)),
                ('date_inscription', models.DateField(auto_now_add=True)),
                ('abonnement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='GestionBibliotheque.abonnement')),
            ],
        ),
        migrations.CreateModel(
            name='Emprunt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_emprunt', models.DateField(auto_now_add=True)),
                ('date_retour_prevue', models.DateField()),
                ('statut', models.CharField(choices=[('en cours', 'En cours'), ('retourné', 'Retourné'), ('en retard', 'En retard')], default='en cours', max_length=20)),
                ('livre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionBibliotheque.livre')),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionBibliotheque.membre')),
            ],
        ),
    ]