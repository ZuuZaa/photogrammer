from django.shortcuts import render, redirect
from photo.forms import PhotoAddForm
from datetime import date
from photo.models import Photo

from django import template
from datetime import date


def add_photo_view(request):
    context = {}

    if request.method == 'POST':
        form = PhotoAddForm(request.POST,request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.img = request.FILES.get('img')
            shared_users = request.POST.getlist('shared_users')
            if shared_users:
                photo.sharing = True
            form.save()
            return redirect('profile')
    else:
        form = PhotoAddForm()

    context['add_photo_form'] = form
    return render(request, 'photo/add_new_photo.html', context)
