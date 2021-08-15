from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

from customuser.models import CustomUser 
from customuser.api.serializers import RegistrationSerializer, UserSerializer

@api_view(['GET', 'POST'])
def api_users_view(request):

    if request.method == 'GET':
        try:
            users_list = CustomUser.objects.all()
        except CustomUser.DoesNotExist:
            return Response(
                {'message':'user is not found'},
                status=status.HTTP_404_NOT_FOUND)
        serializers = UserSerializer(users_list, many=True)
        return Response(data=serializers.data)
    
    elif request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            #token = Token.objects.get(user=account).key
            data['email'] = account.email
            data['first_name'] = account.first_name
            data['last_name'] = account.last_name
            #data['token'] = token
            data['success'] = f'{account.first_name} {account.last_name} sucsessfully registered.'
        else:
            data = serializer.errors
        
        return Response(data)

@api_view(['GET','PUT','DELETE'])
def api_user_detail_view(request, id):
    try:
        user = CustomUser.objects.get(id=id)
    except CustomUser.DoesNotExist:
        return Response(
            {'message':'user is not found'},
            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'update is successful'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        operation = user.delete()
        data = {}
        if operation:
            data['success':'user deleted']
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            data['success':'delete is failed']
            return Response(data=data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
