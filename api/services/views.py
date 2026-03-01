from django.shortcuts import render

from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all().order_by('-date_debut')
    serializer_class = ExperienceSerializer
    

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
    

class CategoriBlogViewSet(viewsets.ModelViewSet):
    queryset = CategoriBlog.objects.all()
    serializer_class = CategoriBlogSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-created_at')
    serializer_class = BlogSerializer
    
    

class TemoignageViewSet(viewsets.ModelViewSet):
    queryset = Temoignage.objects.all()
    serializer_class = TemoignageSerializer
    
    

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('-created_at')
    serializer_class = ContactSerializer
    http_method_names = ['get', 'post', 'head', 'options']
    
    
    

class CategorieProjetViewSet(viewsets.ModelViewSet):
    queryset = CategorieProjet.objects.all()
    serializer_class = CategorieProjetSerializer

class ProjetViewSet(viewsets.ModelViewSet):
    queryset = Projet.objects.all()
    serializer_class = ProjetSerializer
    
    
    

class CategorieProjetViewSet(viewsets.ModelViewSet):
    queryset = CategorieProjet.objects.all()
    serializer_class = CategorieProjetSerializer

class ProjetViewSet(viewsets.ModelViewSet):
    queryset = Projet.objects.all()
    serializer_class = ProjetSerializer