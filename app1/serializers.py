from rest_framework import serializers
from .models import CustomUser, UserProfile
from django.contrib.auth.models import User

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'firstname', 'lastname']
        
class UserProfileSerializer(serializer.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
