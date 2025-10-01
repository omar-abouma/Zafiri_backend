from django.contrib import admin
from .models import StaffMember
from .models import (
    UserProfile,
    GalleryCategory,
    GalleryImage,
    News,
    Event,
    WhyChooseServices,
    ServiceInfrastructure,
)

# --------------------
# UserProfile admin
# --------------------
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')
    search_fields = ('user__username', 'phone')


# --------------------
# Gallery admin
# --------------------
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


# --------------------
# News admin
# --------------------
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


# --------------------
# Events admin
# --------------------
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "location", "start_date", "end_date", "status")
    list_filter = ("status", "start_date", "end_date")
    search_fields = ("title", "location")
    ordering = ("-start_date",)


# --------------------
# Services admin
# --------------------
@admin.register(WhyChooseServices)
class WhyChooseServicesAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "icon")
    search_fields = ("title", "desc")


@admin.register(ServiceInfrastructure)
class ServiceInfrastructureAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("title", "desc")
#----------------------------
# Staff Member admin
#----------------------------
@admin.register(StaffMember)
class StaffAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "gender")
    search_fields = ("name", "position")
    list_filter = ("gender",)