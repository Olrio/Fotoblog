from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin as SecuredView

from . import forms, models

class HomeView(SecuredView, View):
    photos = models.Photo.objects.all()
    template_name = 'blog/home.html'

    def get(self, request):
        return render(request, self.template_name,
        context={'photos': self.photos})

@login_required
def home(request):
    photos = models.Photo.objects.all()
    return render(request, 'blog/home.html',
    context={'photos': photos})

@login_required
def photo_upload(request):
    form = forms.PhotoForm()
    if request.method == 'POST':
        form = forms.PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            photos = models.Photo.objects.all()
            return render(request, 'blog/home.html', {'photos': photos})
    return render(request, 'blog/photo_upload.html',
    context={'form': form})