from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile, GalleryCategory, GalleryImage

class UserProfileTest(TestCase):
    def test_profile_creation(self):
        user = User.objects.create_user(username='testuser', password='pass')
        self.assertTrue(hasattr(user, 'profile'))

class GalleryImageTest(TestCase):
    def setUp(self):
        self.category = GalleryCategory.objects.create(name='Nature')
        self.image = GalleryImage.objects.create(title='Sunset', category=self.category, is_active=True, published=True, image='test.jpg')

    def test_image_str(self):
        self.assertEqual(str(self.image), 'Sunset')
