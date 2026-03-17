from rest_framework import serializers
from ..models import Blog, CategoriBlog

class CategoriBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriBlog
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    categorie_detail = CategoriBlogSerializer(source='categorie', read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'
