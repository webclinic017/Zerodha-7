from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.conf import settings 
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

# from django.contrib.auth import get_user_model
# User = get_user_model

# class showProfileSerializer(ModelSerializer):
#     model = User
#     fields = ('id','username','email',)