from rest_framework import serializers
from django.contrib.auth.models import User
from .models import StaffMember
from .models import Service
from .models import Publication
from .models import (
    GalleryImage, GalleryCategory,
    UserProfile, News, Event,
   
)

# ----------------------------
# User Serializers
# ----------------------------
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        extra_kwargs = {'username': {'required': False}, 'email': {'required': False}}


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    profile_picture = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ['user', 'profile_picture', 'bio', 'phone']

    def get_profile_picture(self, obj):
        if obj.profile_picture:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.profile_picture.url) if request else obj.profile_picture.url
        return None


# ----------------------------
# Gallery Serializers
# ----------------------------
class GalleryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryCategory
        fields = '__all__'


class GalleryImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    category = GalleryCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=GalleryCategory.objects.all(),
        source='category',
        write_only=True,
        allow_null=False,
        required=True
    )

    class Meta:
        model = GalleryImage
        fields = [
            "id",
            "title",
            "description",
            "image",
            "image_url",
            "category",
            "category_id",
            "is_active",
            "published",
            "created_at"
        ]
        extra_kwargs = {
            'category_id': {'required': True}
        }

    def get_image_url(self, obj):
        request = self.context.get("request")
        if obj.image and hasattr(obj.image, "url"):
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None


# ----------------------------
# News Serializer
# ----------------------------
class NewsSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ['id', 'title', 'status', 'date', 'short_text', 'full_text', 'image', 'image_url', 'created_at']

    def get_image_url(self, obj):
        request = self.context.get("request")
        if obj.image:
            return request.build_absolute_uri(obj.image.url) if request else obj.image.url
        return None


# ----------------------------
# Event Serializer
# ----------------------------
class EventSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ["id", "title", "description", "location", "start_date", "end_date", "image", "image_url", "status", "created_at"]

    def get_image_url(self, obj):
        request = self.context.get("request")
        if obj.image:
            return request.build_absolute_uri(obj.image.url) if request else obj.image.url
        return None


# ----------------------------
# Services Serializers
# ----------------------------
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
# ----------------------------
# Staff Member Serializers
# ----------------------------
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffMember
        fields = '__all__'
# ----------------------------
# Publication Serializers  
# ----------------------------
class PublicationSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Publication
        fields = [
            'id', 'author', 'title', 'pub_type', 'date_published',
            'abstract', 'file', 'file_url', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at', 'file_url']

    def get_file_url(self, obj):
        request = self.context.get('request')
        if obj.file and hasattr(obj.file, 'url'):
            if request is not None:
                return request.build_absolute_uri(obj.file.url)
            return obj.file.url
        return None