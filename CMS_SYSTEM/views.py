from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import GalleryImage, GalleryCategory, News, UserProfile
from .forms import GalleryImageForm, UserProfileForm
from .models import Event
# DRF imports
from rest_framework import viewsets, status, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import (
    NewsSerializer,
    GalleryCategorySerializer,
    GalleryImageSerializer,
    UserProfileSerializer,
    UserSerializer,
    EventSerializer,
)

# ----------------------------
# Template-based Views
# ----------------------------
def gallery_home(request):
    categories = GalleryCategory.objects.all()
    images = GalleryImage.objects.filter(is_active=True, published=True).order_by('-created_at')
    return render(request, 'gallery_app/gallery_home.html', {'categories': categories, 'images': images})

@login_required
def upload_image(request):
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery_home')
    else:
        form = GalleryImageForm()
    return render(request, 'gallery_app/upload_image.html', {'form': form})

@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('gallery_home')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'gallery_app/edit_profile.html', {'form': form})

def category_detail(request, category_id):
    category = get_object_or_404(GalleryCategory, id=category_id)
    images = GalleryImage.objects.filter(category=category, is_active=True, published=True)
    return render(request, 'gallery_app/category_detail.html', {'category': category, 'images': images})

# ----------------------------
# NEWS API Views
# ----------------------------
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-created_at')
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticated]   # ili tusichanganye public na admin

from rest_framework.permissions import AllowAny

class PublicNewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.filter(status='published').order_by('-created_at')
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]

    #gallery viewssets
class GalleryCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GalleryCategory.objects.all()
    serializer_class = GalleryCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class GalleryImageViewSet(viewsets.ModelViewSet):
    queryset = GalleryImage.objects.filter(is_active=True, published=True)
    serializer_class = GalleryImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'title']

# ----------------------------
# User Profile APIs
# ----------------------------
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    """
    GET → return user + profile
    PUT → update user + profile
    """
    try:
        profile = request.user.profile
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)

    if request.method == 'GET':
        return Response({
            'user': UserSerializer(request.user, context={'request': request}).data,
            'profile': UserProfileSerializer(profile, context={'request': request}).data
        })
    elif request.method == 'PUT':
        user_serializer = UserSerializer(request.user, data=request.data.get('user', {}), partial=True)
        profile_serializer = UserProfileSerializer(profile, data=request.data.get('profile', {}), partial=True, context={'request': request})

        if user_serializer.is_valid() and profile_serializer.is_valid():
            user_serializer.save()
            profile_serializer.save()
            return Response({
                'user': user_serializer.data,
                'profile': profile_serializer.data
            })
        return Response({
            'user_errors': user_serializer.errors,
            'profile_errors': profile_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    """GET-only (backward compatible)"""
    try:
        profile = request.user.profile
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)
    return Response({
        'user': UserSerializer(request.user, context={'request': request}).data,
        'profile': UserProfileSerializer(profile, context={'request': request}).data
    })

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_profile_picture(request):
    """Update profile picture only"""
    try:
        profile = request.user.profile
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)

    picture = request.FILES.get('profile_picture')
    if picture:
        profile.profile_picture = picture
        profile.save()

    return Response(UserProfileSerializer(profile, context={'request': request}).data)

# ----------------------------
# JWT login (CSRF-exempt)
# ----------------------------
@method_decorator(csrf_exempt, name='dispatch')
class CsrfExemptTokenObtainPairView(TokenObtainPairView):
    pass

# ----------------------------
# Event ViewSet
# ----------------------------

# CMS management (admin/editor)
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by("-start_date")
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context
    
class PublicEventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.filter(status="published").order_by("-start_date")
    serializer_class = EventSerializer
    permission_classes = [AllowAny]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context
