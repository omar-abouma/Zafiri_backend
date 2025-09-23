from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet, GalleryCategoryViewSet, GalleryImageViewSet, user_profile, get_user_profile
from .views import PublicNewsViewSet
from .views import EventViewSet, PublicEventViewSet

router = DefaultRouter()
router.register(r'news', NewsViewSet, basename='news')
router.register(r'public-news', PublicNewsViewSet, basename='public-news')
router.register(r'gallery-categories', GalleryCategoryViewSet, basename='gallery-categories')
router.register(r'gallery-images', GalleryImageViewSet, basename='gallery-images')
router.register(r'events', EventViewSet, basename="events")          # CMS protected
router.register(r'public-events', PublicEventViewSet, basename="public-events")  # Public

urlpatterns = [
    # API endpoints
    path('api/', include(router.urls)),
    path('api/profile/', get_user_profile, name='get_user_profile'),  # New endpoint
    path('api/user-profile/', user_profile, name='user_profile'),     # Existing endpoint

    path('api/profile-picture/', views.update_profile_picture, name='update_profile_picture'),
    path('api/login/', views.CsrfExemptTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/events/', EventViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/public-events/', PublicEventViewSet.as_view({'get': 'list'})),

    # Template views
    path('', views.gallery_home, name='gallery_home'),
    path('upload/', views.upload_image, name='upload_image'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
]