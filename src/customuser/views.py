from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from customuser.forms import RegistrationForm, AccountAuthenticationForm
from customuser.models import CustomUser
from photo.models import Photo


def register_view(request):
    context = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            messages.info(request, f'Welcome, {first_name} {last_name}.')
            return redirect('home')
    else:
        form = RegistrationForm()
    context['register_form'] = form
    return render(request, 'account/register.html', context)


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
               # messages.info(request, 'Welcome back.')
                login(request, user)
                return redirect('home')
    else:
        form = AccountAuthenticationForm()
    context['login_form'] = form
    return render(request, "account/login.html", context)


def logout_view(request):
    logout(request)
    return redirect('home')


def profile_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        context = {}
        user = request.user
        photos = Photo.objects.filter(user=user.id)
        context['user'] = user
        context['photos'] = photos
        return render(request, 'account/profile.html', context)


def user_profile_view(request, slug):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        user = request.user
        context = {}
        profile = CustomUser.objects.filter(slug=slug).last()
        if profile:
            photos = Photo.objects.filter(sharing=True, user=profile)
            context['user'] = user
            context['profile'] = profile
            context['photos'] = photos
            return render(request, 'account/user.html', context)
        else:
            return redirect('home')

