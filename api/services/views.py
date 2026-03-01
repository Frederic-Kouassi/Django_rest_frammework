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