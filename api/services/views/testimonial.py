from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Temoignage
from ..serializers.testimonial import TemoignageSerializer

class TestimonialListView(APIView):
    def get(self, request):
        testimonials = Temoignage.objects.all()
        serializer = TemoignageSerializer(testimonials, many=True)
        return Response(serializer.data)
