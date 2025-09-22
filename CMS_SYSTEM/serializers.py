from rest_framework import serializers
from django.contrib.auth.models import User
from .models import GalleryImage, GalleryCategory, UserProfile, News

# ----------------------------
# User Serializer
# ----------------------------
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        extra_kwargs = {
            'username': {'required': False},
            'email': {'required': False},
        }

# ----------------------------
# Gallery Serializers
# ----------------------------
class GalleryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryCategory
        fields = ['id', 'name', 'description', 'created_at']

class GalleryImageSerializer(serializers.ModelSerializer):
    category = GalleryCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=GalleryCategory.objects.all(),
        source='category',
        write_only=True,
        required=False,
        allow_null=True
    )
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = GalleryImage
        fields = [
            'id', 'title', 'description', 'image', 'image_url',
            'category', 'category_id', 'is_active', 'published',
            'created_at', 'updated_at'
        ]

    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None

# ----------------------------
# UserProfile Serializer
# ----------------------------
class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    profile_picture = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ['user', 'profile_picture', 'bio', 'phone']

    def get_profile_picture(self, obj):
        if obj.profile_picture:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.profile_picture.url)
            return obj.profile_picture.url
        return None

# ----------------------------
# News Serializer
# ----------------------------
class NewsSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = [
            'id', 'title', 'status', 'date',
            'short_text', 'full_text',
            'image', 'image_url', 'created_at'
        ]

    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None