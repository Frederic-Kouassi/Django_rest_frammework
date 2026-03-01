from rest_framework import serializers
from .models import *

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'
        

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        

class CategoriBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriBlog
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    categorie_detail = CategoriBlogSerializer(source='categorie', read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'
        

class TemoignageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temoignage
        fields = '__all__'
        

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        
        
        

class CategorieProjetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategorieProjet
        fields = '__all__'

class ProjetSerializer(serializers.ModelSerializer):
    categorie_detail = CategorieProjetSerializer(source='categorie', read_only=True)

    class Meta:
        model = Projet
        fields = '__all__'
        

class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profil
        fields = '__all__'