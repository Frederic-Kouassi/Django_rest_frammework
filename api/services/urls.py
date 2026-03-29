from rest_framework.routers import DefaultRouter
from django.urls import path
from .views.experience import ExperienceListView
from .views.service import ServiceListView
from .views.blog import BlogListView, BlogCategoryListView
from .views.contact import ContactCreateView
from .views.project import ProjectListView, ProjectCategoryListView
from .views.profile import ProfileDetailView
from .views.testimonial import TestimonialListView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('experience/', ExperienceListView.as_view(), name='experience-list'),
    path('service/', ServiceListView.as_view(), name='service-list'),
    path('blog/', BlogListView.as_view(), name='blog-list'),
    path('blog/categories/', BlogCategoryListView.as_view(), name='blog-category-list'),
    path('contact/', ContactCreateView.as_view(), name='contact-create'),
    path('project/', ProjectListView.as_view(), name='project-list'),
    path('project/categories/', ProjectCategoryListView.as_view(), name='project-category-list'),
    path('profil/', ProfileDetailView.as_view(), name='profile-detail'),
    path('testimonial/', TestimonialListView.as_view(), name='testimonial-list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
urlpatterns += staticfiles_urlpatterns()


