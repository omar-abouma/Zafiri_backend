from django.contrib import admin
from .models import UserProfile, GalleryCategory, GalleryImage, News

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')
    search_fields = ('user__username', 'phone')

@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_active', 'published', 'created_at')
    list_filter = ('category', 'is_active', 'published')
    search_fields = ('title', 'description')
    list_editable = ('is_active', 'published')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "date", "created_at")
    search_fields = ("title", "short_text", "full_text")
    list_filter = ("status", "date")
    ordering = ("-date",)
    fieldsets = (
        (None, {"fields": ("title", "status", "date", "image")}),
        ("Content", {"fields": ("short_text", "full_text")}),
    )