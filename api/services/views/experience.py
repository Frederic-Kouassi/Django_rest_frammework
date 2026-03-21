from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Experience
from ..serializers.experience import ExperienceSerializer

class ExperienceListView(APIView):
    def get(self, request):
        experiences = Experience.objects.all().order_by('-date_debut')
        serializer = ExperienceSerializer(experiences, many=True)
        return Response(serializer.data)
