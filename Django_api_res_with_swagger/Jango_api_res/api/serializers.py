from rest_framework import serializers
from .models import Cat_Res,Restaurant,Iteams
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['id','username','email','first_name','last_name']


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Restaurant
        fields='__all__'


class Cat_resSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cat_Res
        fields='__all__'
   

class IteamSSerializer(serializers.ModelSerializer):
    class Meta:
        model=Iteams
        fields='__all__'

