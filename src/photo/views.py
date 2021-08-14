from django.shortcuts import render
from photo.forms import PhotoAddForm


def add_photo_view(request):
    context = {}
    if request.method == 'POST':
        form = PhotoAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = PhotoAddForm()
    context['add_photo_form'] = form
    return render(request, 'photo/add_new_photo.html', context)
