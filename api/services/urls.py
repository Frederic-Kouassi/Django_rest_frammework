from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *

router = DefaultRouter()
router.register(r'experiences', ExperienceViewSet, basename='experience')
router.register(r'services', ServiceViewSet, basename='service')
router.register(r'blog/categories', CategoriBlogViewSet, basename='categori-blog')
router.register(r'blogs', BlogViewSet, basename='blog')
router.register(r'temoignages', TemoignageViewSet, basename='temoignage')


router.register(r'projets/categories', CategorieProjetViewSet, basename='categorie-projet')
router.register(r'projets', ProjetViewSet, basename='projet')



urlpatterns = [
    path('', include(router.urls)),
    path('contacts/', ContactView.as_view(), name='contact-list'),
    path('contacts/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
]