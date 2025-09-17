from rest_framework import serializers
from .models import GalleryImage, GalleryCategory, UserProfile

class GalleryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryCategory
        fields = ['id', 'name', 'description', 'created_at']

class GalleryImageSerializer(serializers.ModelSerializer):
    category = GalleryCategorySerializer(read_only=True)
    class Meta:
        model = GalleryImage
        fields = ['id', 'title', 'description', 'image', 'category', 'is_active', 'published', 'created_at', 'updated_at']

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = UserProfile
        fields = ['user', 'profile_picture', 'bio', 'phone']
