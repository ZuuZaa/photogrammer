from rest_framework import serializers
from photo.models import Photo

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = [
            'img', 
            'user', 
            'description', 
            'shared_users',
            'sharing_end_date'
            ]
