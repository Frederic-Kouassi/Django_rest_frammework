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