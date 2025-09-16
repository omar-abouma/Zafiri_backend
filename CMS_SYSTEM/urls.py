from django.urls import path
from . import views

urlpatterns = [
    # Authentication
    path('login/', views.CustomAuthToken.as_view(), name='api-login'),
    path('update-profile-picture/', views.update_profile_picture, name='update-profile-picture'),

    # Gallery Endpoints
    path('gallery/categories/', views.GalleryCategoryListCreateView.as_view(), name='gallery-category-list-create'),
    path('gallery/categories/<int:pk>/', views.GalleryCategoryDetailView.as_view(), name='gallery-category-detail'),
    path('gallery/images/', views.GalleryImageListCreateView.as_view(), name='gallery-image-list-create'),
    path('gallery/images/<int:pk>/', views.GalleryImageDetailView.as_view(), name='gallery-image-detail'),
    path('gallery/public/', views.PublicGalleryImageView.as_view(), name='public-gallery'),

    # News
    path('news/', views.NewsListCreateView.as_view(), name='news-list-create'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='news-detail'),

    # Events
    path('events/', views.EventListCreateView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),

    # Projects
    path('projects/', views.ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),

    # Publications
    path('publications/', views.PublicationListCreateView.as_view(), name='publication-list-create'),
    path('publications/<int:pk>/', views.PublicationDetailView.as_view(), name='publication-detail'),

    # Research
    path('research/', views.ResearchListCreateView.as_view(), name='research-list-create'),
    path('research/<int:pk>/', views.ResearchDetailView.as_view(), name='research-detail'),

    # Services
    path('services/', views.ServiceListCreateView.as_view(), name='service-list-create'),
    path('services/<int:pk>/', views.ServiceDetailView.as_view(), name='service-detail'),
]
