from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from photo.models import Photo
from photo.api.serializers import PhotoSerializer

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated),)
def api_photos_view(request):

    if request.method == 'GET':
        try:
            photo_list = Photo.objects.all()
        except Photo.DoesNotExist:
            return Response(
                {'message':'photo is not found'},
                status=status.HTTP_404_NOT_FOUND)
        serializers = PhotoSerializer(photo_list, many=True)
        return Response(data=serializers.data)
    
    elif request.method == 'POST':
        pass
        # serializer = PhotoSerializer(data=request.data)
        # data = {}
        # if serializer.is_valid():
        #     photo = serializer.save()
        # else:
        #     data = serializer.errors
        # return Response(data)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated),)
def api_photo_detail_view(request, id):
    try:
        photo = Photo.objects.get(id=id)
    except Photo.DoesNotExist:
        return Response(
            {'message':'photo is not found'},
            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PhotoSerializer(photo)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        if photo.user != request.user:
            data['response'] = "You don't have permission to edit that."
            return Response(data=data)        
        else:
            serializer = PhotoSerializer(photo, data=request.data)
            data = {}
            if serializer.is_valid():
                seriliser.user = request.user
                serializer.save()
                data['success'] = 'update is successful'
                return Response(data=data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        if photo.user != request.user:
            data['response'] = "You don't have permission to edit that."
            return Response(data=data) 
        else:
            operation = photo.delete()
            data = {}
            if operation:
                data['success':'photo deleted']
                return Response(status=status.HTTP_204_NO_CONTENT, data=data)
            else:
                data['success':'delete is failed']
                return Response(status=status.HTTP_400_BAD_REQUEST, data=data)

