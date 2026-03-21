from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Blog, CategoriBlog
from ..serializers.blog import BlogSerializer, CategoriBlogSerializer

class BlogListView(APIView):
    def get(self, request):
        blogs = Blog.objects.all().order_by('-created_at')
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

class BlogCategoryListView(APIView):
    def get(self, request):
        categories = CategoriBlog.objects.all()
        serializer = CategoriBlogSerializer(categories, many=True)
        return Response(serializer.data)
