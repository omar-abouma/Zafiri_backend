from django.db import models
from django.contrib.auth.models import User

# --------------------
# User Profile
# --------------------
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


# Auto-create and save profile
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def manage_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        # if profile exists just save in case of changes
        try:
            instance.profile.save()
        except Exception:
            # in rare cases profile might not exist
            UserProfile.objects.get_or_create(user=instance)


# --------------------
# Gallery
# --------------------
class GalleryCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    category = models.ForeignKey(GalleryCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name="images")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="gallery_images/")
    is_active = models.BooleanField(default=True)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# --------------------
# News
# --------------------
class News(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=200)
    short_text = models.TextField()
    full_text = models.TextField()
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title


# --------------------
# Events
# --------------------
class Event(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    image = models.ImageField(upload_to="events/", blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        return self.title


# --------------------
# Services model
# --------------------
class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='service_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
#---------------------------
# organization staff models
#---------------------------
class StaffMember(models.Model):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]

    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    bio = models.TextField()
    image = models.ImageField(upload_to="staff_images/")

    def __str__(self):
        return self.name
#---------------------------
# Publication model
#---------------------------
class Publication(models.Model):
    """
    Publication model with file upload.
    """
    TYPE_CHOICES = [
        ('Journal Article', 'Journal Article'),
        ('Conference Paper', 'Conference Paper'),
        ('Book Chapter', 'Book Chapter'),
        ('Report', 'Report'),
        ('Other', 'Other'),
    ]

    author = models.CharField(max_length=255)
    title = models.TextField()
    pub_type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='Other')
    date_published = models.DateField()
    abstract = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='publications/%Y/%m/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_published', '-created_at']
        verbose_name = "Publication"
        verbose_name_plural = "Publications"

    def __str__(self):
        return f"{self.title} — {self.author}"
# -------------------------
# organization structure models
# -------------------------

class OrganizationStructureFile(models.Model):
    FILE_TYPES = (
        ('pdf', 'PDF'),
        ('image', 'Image'),
    )

    # Ruhusu null=True, blank=True ili migration ipite (baadae unaweza kuondoa)
    file = models.FileField(upload_to='organization_structure/', null=True, blank=True)
    file_type = models.CharField(max_length=10, choices=FILE_TYPES, blank=True)
    original_name = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.file:
            if not self.original_name:
                self.original_name = self.file.name
            if self.file.name.lower().endswith('.pdf'):
                self.file_type = 'pdf'
            else:
                self.file_type = 'image'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.original_name or "No File"
    
#----------------------------
# Home page models
#----------------------------
from django.db import models

class HomeSlide(models.Model):
    image = models.ImageField(upload_to='slides/')
    text = models.TextField()
    order_index = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Slide {self.id} - {self.text[:30]}"


class HomeViceChancellorMessage(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='vc/images/')
    video = models.FileField(upload_to='vc/videos/', blank=True, null=True)  # store video file
    message_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class HomeService(models.Model):
    image = models.ImageField(upload_to='services/')
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class HomeMarineSection(models.Model):
    image = models.ImageField(upload_to='marine/')
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class HomeEvent(models.Model):
    image = models.ImageField(upload_to='events/')
    date = models.DateField()
    title = models.CharField(max_length=255)
    subtitle = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    badge = models.CharField(max_length=100, default='ZAFIRI')

    def __str__(self):
        return self.title


class HomeImpactOverview(models.Model):
    VISITOR = 'visitors'
    PUBLICATION = 'publications'
    PROJECT = 'projects'
    EVENT = 'events'

    TYPE_CHOICES = [
        (VISITOR, 'Visitors'),
        (PUBLICATION, 'Publications'),
        (PROJECT, 'Projects'),
        (EVENT, 'Events'),
    ]

    impact_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    icon = models.ImageField(upload_to='impact/')
    title = models.CharField(max_length=255)
    description = models.TextField()
    target = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title} ({self.impact_type})"
