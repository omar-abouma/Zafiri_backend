from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StaffViewSet
from .views import (
    # News
    NewsViewSet, PublicNewsViewSet,

    # Events
    EventViewSet, PublicEventViewSet,

    # Gallery
    PublicGalleryImageViewSet, PublicGalleryCategoryViewSet,
    GalleryImageAdminViewSet, GalleryCategoryAdminViewSet,

    # User/Profile
    user_profile, get_user_profile, update_profile_picture, CsrfExemptTokenObtainPairView,
    upload_image, gallery_home, edit_profile, category_detail
)
from .views import (
    WhyChooseServicesAdminViewSet,
    ServiceInfrastructureAdminViewSet,
    WhyChooseServicesPublicViewSet,
    ServiceInfrastructurePublicViewSet,
)

router = DefaultRouter()

# --------------------
# News
# --------------------
router.register(r'news', NewsViewSet, basename='news')                     # CMS (full CRUD)
router.register(r'public-news', PublicNewsViewSet, basename='public-news') # Public (readonly)

# --------------------
# Events
# --------------------
router.register(r'events', EventViewSet, basename="events")                # CMS
router.register(r'public-events', PublicEventViewSet, basename="public-events")  # Public

# --------------------
# Gallery
# --------------------
# Admin
router.register("gallery", GalleryImageAdminViewSet, basename="gallery")
router.register("gallery-categories", GalleryCategoryAdminViewSet, basename="gallery-categories")
# Public
router.register("public-gallery", PublicGalleryImageViewSet, basename="public-gallery")
router.register("public-gallery-categories", PublicGalleryCategoryViewSet, basename="public-gallery-categories")

# --------------------
# Services
# --------------------
# Admin
router.register(r'admin-whychoose', WhyChooseServicesAdminViewSet, basename='admin-whychoose')
router.register(r'admin-infrastructure', ServiceInfrastructureAdminViewSet, basename='admin-infrastructure')

# Public
router.register(r'public-whychoose', WhyChooseServicesPublicViewSet, basename='public-whychoose')
router.register(r'public-infrastructure', ServiceInfrastructurePublicViewSet, basename='public-infrastructure')
# ----------------------------
# Staff Members 
# ----------------------------
router.register(r"staff", StaffViewSet, basename="staff")


urlpatterns = [
    # API endpoints
    path('api/', include(router.urls)),

    # Profile endpoints
    path('api/profile/', get_user_profile, name='get_user_profile'),
    path('api/user-profile/', user_profile, name='user_profile'),
    path('api/profile-picture/', update_profile_picture, name='update_profile_picture'),

    # Auth
    path('api/login/', CsrfExemptTokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Template views (if using Django templates still)
    path('', gallery_home, name='gallery_home'),
    path('upload/', upload_image, name='upload_image'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('category/<int:category_id>/', category_detail, name='category_detail'),
]
