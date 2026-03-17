from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Profil
from ..serializers.profile import ProfilSerializer

class ProfileDetailView(APIView):
    def get(self, request):
        # Assuming there's only one profile for the portfolio
        profile = Profil.objects.first()
        if profile:
            serializer = ProfilSerializer(profile)
            return Response(serializer.data)
        return Response({"detail": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)
