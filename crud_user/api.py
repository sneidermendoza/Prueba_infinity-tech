from rest_framework.response import Response
from rest_framework import status
from .models import User
from rest_framework.decorators import api_view
from .serializers import UserSerializer, UserListSerializer


@api_view(['GET', 'POST'])
def user_api_view(request):
    if request.method == 'GET':
        # queryset
        users = User.objects.all().values('id','first_name','last_name','date_birth','address','password', 'mobile_phone')
        users_serializer = UserListSerializer(users,many = True)
        
        return Response(users_serializer.data, status = status.HTTP_200_OK)
    
    # create
    elif request.method == 'POST':
        user_serializer = UserSerializer(data = request.data)
        # validation
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status = status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_api_view(request, pk):

    # queryset
    user = User.objects.filter(id = pk).first()

    # validation
    if user:

        # get user
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status = status.HTTP_200_OK)

        # update
        elif request.method == 'PUT':
            user = User.objects.filter(id = pk).first()
            user_serializer = UserSerializer(user, data = request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status = status.HTTP_200_OK)
            return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        # delete
        elif request.method == 'DELETE':
            user = User.objects.filter(id = pk).first()
            user_serializer = UserSerializer(user)
            user.delete()
            return Response(user_serializer.data, status = status.HTTP_200_OK)

    return Response({'message': 'No user found with this data...'}, status = status.HTTP_400_BAD_REQUEST)