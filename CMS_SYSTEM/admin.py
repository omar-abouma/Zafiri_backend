from django.contrib import admin
from .models import StaffMember
from .models import Publication
from .models import OrganizationStructureFile
from .models import (
    UserProfile,
    GalleryCategory,
    GalleryImage,
    News,
    Event,
   
)
from .models import Service
from .models import (
    HomeSlide, HomeViceChancellorMessage, HomeService,
    HomeMarineSection, HomeEvent, HomeImpactOverview
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
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')  # columns to show
    list_display_links = ('title',)  # make title clickable
    search_fields = ('title', 'description')  # search box
    list_filter = ('created_at', 'updated_at')  # filter sidebar
    ordering = ('-created_at',)  # newest first
    readonly_fields = ('created_at', 'updated_at')  # cannot edit these
#----------------------------
# Staff Member admin
#----------------------------
@admin.register(StaffMember)
class StaffAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "gender")
    search_fields = ("name", "position")
    list_filter = ("gender",)
# --------------------
# Publication admin 
# --------------------
@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'pub_type', 'date_published', 'file_present')
    list_filter = ('pub_type', 'date_published')
    search_fields = ('title', 'author', 'abstract')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-date_published',)

    def file_present(self, obj):
        return bool(obj.file)
    file_present.boolean = True
    file_present.short_description = 'Has File'
#----------------------------
# Organization Structure admin
#----------------------------
@admin.register(OrganizationStructureFile)
class OrganizationStructureFileAdmin(admin.ModelAdmin):
    list_display = ('original_name', 'file_type', 'uploaded_at')
    readonly_fields = ('uploaded_at',)

# -----------------------------
# HomeSlide Admin
# -----------------------------
@admin.register(HomeSlide)
class HomeSlideAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'order_index', 'is_active', 'created_at', 'updated_at')
    list_editable = ('order_index', 'is_active')
    ordering = ('order_index',)
    search_fields = ('text',)


# -----------------------------
# HomeViceChancellorMessage Admin
# -----------------------------
@admin.register(HomeViceChancellorMessage)
class HomeVCMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'created_at', 'updated_at')
    search_fields = ('name', 'title')


# -----------------------------
# HomeService Admin
# -----------------------------
@admin.register(HomeService)
class HomeServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')
    search_fields = ('title',)


# -----------------------------
# HomeMarineSection Admin
# -----------------------------
@admin.register(HomeMarineSection)
class HomeMarineAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')
    search_fields = ('title',)


# -----------------------------
# HomeEvent Admin
# -----------------------------
@admin.register(HomeEvent)
class HomeEventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'badge', 'uploaded_at')
    list_filter = ('date', 'badge')
    search_fields = ('title', 'subtitle')


# -----------------------------
# HomeImpactOverview Admin
# -----------------------------
@admin.register(HomeImpactOverview)
class HomeImpactOverviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'impact_type', 'target')
    list_filter = ('impact_type',)
    search_fields = ('title',)