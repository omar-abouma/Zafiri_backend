from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import GalleryImage, GalleryCategory
from .forms import GalleryImageForm, UserProfileForm

def gallery_home(request):
    categories = GalleryCategory.objects.all()
    images = GalleryImage.objects.filter(is_active=True, published=True).order_by('-created_at')
    return render(request, 'gallery_app/gallery_home.html', {'categories': categories, 'images': images})

@login_required
def upload_image(request):
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery_home')
    else:
        form = GalleryImageForm()
    return render(request, 'gallery_app/upload_image.html', {'form': form})

@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('gallery_home')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'gallery_app/edit_profile.html', {'form': form})

def category_detail(request, category_id):
    category = get_object_or_404(GalleryCategory, id=category_id)
    images = GalleryImage.objects.filter(category=category, is_active=True, published=True)
    return render(request, 'gallery_app/category_detail.html', {'category': category, 'images': images})
