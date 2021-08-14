from django.urls import path
from photo.api.views import api_photo_detail_view, api_photos_view

urlpatterns = [
    path('<int:id>', api_photo_detail_view, name='user_detail'),
    path('', api_photos_view, name='users')
]