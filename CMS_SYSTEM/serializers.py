from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *

User = get_user_model()

# User
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)
    class Meta:
        model = User
        fields = ['id','username','email','first_name','last_name','profile']

# Gallery
class GalleryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryCategory
        fields = '__all__'

class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = '__all__'

class PublicGalleryImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    category_name = serializers.CharField(source='category.name', read_only=True)
    class Meta:
        model = GalleryImage
        fields = ['id','title','image_url','category_name','description','created_at']
    def get_image_url(self,obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None

# Other Models
class NewsSerializer(serializers.ModelSerializer):
    class Meta: model = News; fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta: model = Event; fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta: model = Project; fields = '__all__'

class PublicationSerializer(serializers.ModelSerializer):
    class Meta: model = Publication; fields = '__all__'

class ResearchSerializer(serializers.ModelSerializer):
    class Meta: model = Research; fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta: model = Service; fields = '__all__'
