from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Contact

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
    
    
class ContactView(APIView):

    # GET tous les contacts
    def get(self, request):
        contacts = Contact.objects.all().order_by('-created_at')
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

    # POST créer un contact
    def post(self, request):
        serializer = ContactSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class ContactDetailView(APIView):

    def get_object(self, pk):
        try:
            return Contact.objects.get(pk=pk)
        except Contact.DoesNotExist:
            return None

    # GET un contact
    def get(self, request, pk):
        contact = self.get_object(pk)

        if not contact:
            return Response({"error": "Contact non trouvé"}, status=404)

        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    # PUT modifier
    def put(self, request, pk):
        contact = self.get_object(pk)

        if not contact:
            return Response({"error": "Contact non trouvé"}, status=404)

        serializer = ContactSerializer(contact, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    # DELETE supprimer
    def delete(self, request, pk):
        contact = self.get_object(pk)

        if not contact:
            return Response({"error": "Contact non trouvé"}, status=404)

        contact.delete()
        return Response({"message": "Contact supprimé"}, status=204)
    



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