from django.urls import path, include
from photo.views import add_photo_view

urlpatterns = [
    path('api/', include('photo.api.urls')),
    path('add', add_photo_view, name='add_photo'),
]