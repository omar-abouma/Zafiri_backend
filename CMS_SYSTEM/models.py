from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# User Profile
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()

# Gallery
class GalleryCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class GalleryImage(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='gallery/')
    category = models.ForeignKey(GalleryCategory, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    def __str__(self):
        return self.title

# News
class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)
    def __str__(self):
        return self.title

# Event
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

# Project
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    def __str__(self):
        return self.name

# Publication
class Publication(models.Model):
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    authors = models.CharField(max_length=200)
    published_date = models.DateField()
    document = models.FileField(upload_to='publications/', null=True, blank=True)
    def __str__(self):
        return self.title

# Research
class Research(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    lead_researcher = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=[('Ongoing','Ongoing'), ('Completed','Completed')])
    def __str__(self):
        return self.title

# Service
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50)
    def __str__(self):
        return self.name
