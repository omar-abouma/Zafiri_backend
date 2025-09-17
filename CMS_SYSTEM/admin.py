from django.contrib import admin
from .models import UserProfile, GalleryCategory, GalleryImage

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')

@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_active', 'published', 'created_at')
    list_filter = ('category', 'is_active', 'published')
    search_fields = ('title', 'description')
