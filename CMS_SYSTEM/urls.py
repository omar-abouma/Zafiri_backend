from django.urls import path
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    # Regular website views
    path('', views.gallery_home, name='gallery_home'),
    path('upload/', views.upload_image, name='upload_image'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),

    # HTML login/logout pages (Django built-in auth views)
    path('login/', auth_views.LoginView.as_view(template_name='gallery_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='gallery_home'), name='logout'),

    # API login/logout using JWT tokens (for REST clients)
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
