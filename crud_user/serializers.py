from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        
    def to_representation(self,instance):
        return {
        'id' :instance['id'],
        'first_name': instance['first_name'],
        'last_name':instance['last_name'],
        'date_birth': instance['date_birth'],
        'address': instance['address'],
        'password': instance['password'],
        'mobile_phone': instance['mobile_phone']
        }