from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from CMS_SYSTEM.views import CsrfExemptTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT Authentication
    path('api/login/', CsrfExemptTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Main App
    path('', include('CMS_SYSTEM.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)