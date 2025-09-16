from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .models import *
from .serializers import *

# --- Authentication ---
class CustomAuthToken(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        profile_picture = None
        if hasattr(user,'profile') and user.profile.profile_picture:
            profile_picture = request.build_absolute_uri(user.profile.profile_picture.url)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'profile_picture': profile_picture
        })

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_profile_picture(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if 'profile_picture' in request.FILES:
        profile.profile_picture = request.FILES['profile_picture']
        profile.save()
        return Response({'profile_picture': request.build_absolute_uri(profile.profile_picture.url)})
    return Response({'error':'No image provided'},status=status.HTTP_400_BAD_REQUEST)

# --- Gallery ---
class GalleryCategoryListCreateView(generics.ListCreateAPIView):
    queryset = GalleryCategory.objects.all()
    serializer_class = GalleryCategorySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class GalleryCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GalleryCategory.objects.all()
    serializer_class = GalleryCategorySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class GalleryImageListCreateView(generics.ListCreateAPIView):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class GalleryImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class PublicGalleryImageView(generics.ListAPIView):
    queryset = GalleryImage.objects.filter(published=True).order_by('-created_at')
    serializer_class = PublicGalleryImageSerializer
    permission_classes = [AllowAny]

# --- News ---
class NewsListCreateView(generics.ListCreateAPIView):
    queryset = News.objects.all().order_by('-published_date')
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticated]

class NewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticated]

class PublicNewsView(generics.ListAPIView):
    queryset = News.objects.all().order_by('-published_date')
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]

# --- Event ---
class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all().order_by('-date')
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

class PublicEventView(generics.ListAPIView):
    queryset = Event.objects.all().order_by('-date')
    serializer_class = EventSerializer
    permission_classes = [AllowAny]

# --- Project ---
class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all().order_by('-start_date')
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

class PublicProjectView(generics.ListAPIView):
    queryset = Project.objects.all().order_by('-start_date')
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]

# --- Publication ---
class PublicationListCreateView(generics.ListCreateAPIView):
    queryset = Publication.objects.all().order_by('-published_date')
    serializer_class = PublicationSerializer
    permission_classes = [IsAuthenticated]

class PublicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    permission_classes = [IsAuthenticated]

class PublicPublicationView(generics.ListAPIView):
    queryset = Publication.objects.all().order_by('-published_date')
    serializer_class = PublicationSerializer
    permission_classes = [AllowAny]

# --- Research ---
class ResearchListCreateView(generics.ListCreateAPIView):
    queryset = Research.objects.all()
    serializer_class = ResearchSerializer
    permission_classes = [IsAuthenticated]

class ResearchDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Research.objects.all()
    serializer_class = ResearchSerializer
    permission_classes = [IsAuthenticated]

class PublicResearchView(generics.ListAPIView):
    queryset = Research.objects.all()
    serializer_class = ResearchSerializer
    permission_classes = [AllowAny]

# --- Service ---
class ServiceListCreateView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]

class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]

class PublicServiceView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [AllowAny]
