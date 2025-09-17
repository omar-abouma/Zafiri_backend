from django import forms
from .models import UserProfile, GalleryImage

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'bio', 'phone']

class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['title', 'description', 'image', 'category', 'is_active', 'published']
