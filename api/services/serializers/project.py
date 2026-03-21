from rest_framework import serializers
from ..models import Projet, CategorieProjet

class CategorieProjetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategorieProjet
        fields = '__all__'

class ProjetSerializer(serializers.ModelSerializer):
    categorie_detail = CategorieProjetSerializer(source='categorie', read_only=True)

    class Meta:
        model = Projet
        fields = '__all__'
