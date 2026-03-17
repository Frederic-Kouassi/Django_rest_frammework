from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Projet, CategorieProjet
from ..serializers.project import ProjetSerializer, CategorieProjetSerializer

class ProjectListView(APIView):
    def get(self, request):
        projects = Projet.objects.all()
        serializer = ProjetSerializer(projects, many=True)
        return Response(serializer.data)

class ProjectCategoryListView(APIView):
    def get(self, request):
        categories = CategorieProjet.objects.all()
        serializer = CategorieProjetSerializer(categories, many=True)
        return Response(serializer.data)
