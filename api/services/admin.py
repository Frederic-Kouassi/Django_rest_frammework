from django.contrib import admin
from .models import *

# -------------------------------
# Experience
# -------------------------------
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'titre', 'compagnie', 'position', 'pays', 'date_debut', 'date_fin')
    search_fields = ('titre', 'compagnie', 'position', 'pays')
    list_filter = ('date_debut', 'date_fin', 'pays')


# -------------------------------
# Service
# -------------------------------
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'description')
    search_fields = ('nom',)


# -------------------------------
# CategoriBlog
# -------------------------------
@admin.register(CategoriBlog)
class CategoriBlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom')
    search_fields = ('nom',)


# -------------------------------
# Blog
# -------------------------------
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'titre', 'auteur', 'categorie', 'created_at')
    search_fields = ('titre', 'auteur')
    list_filter = ('categorie', 'created_at')


# -------------------------------
# Temoignage
# -------------------------------
@admin.register(Temoignage)
class TemoignageAdmin(admin.ModelAdmin):
    list_display = ('id', 'titre', 'position', 'etoiles')
    search_fields = ('titre', 'position')
    list_filter = ('etoiles',)


# -------------------------------
# Contact
# -------------------------------
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'email', 'created_at')
    search_fields = ('nom', 'email')
    list_filter = ('created_at',)


# -------------------------------
# CategorieProjet
# -------------------------------
@admin.register(CategorieProjet)
class CategorieProjetAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'type_projet')
    search_fields = ('nom', 'type_projet')


# -------------------------------
# Projet
# -------------------------------
@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ('id', 'titre', 'categorie', 'technologies')
    search_fields = ('titre', 'technologies')
    list_filter = ('categorie',)


# -------------------------------
# Profil
# -------------------------------
@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ('id', 'prenom', 'nom', 'titre', 'email', 'disponible', 'années_experience')
    search_fields = ('nom', 'prenom', 'email', 'titre')
    list_filter = ('disponible',)