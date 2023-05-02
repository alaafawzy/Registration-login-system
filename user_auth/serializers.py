from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'phone_number', 'email' ,'gender')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'phone_number', 'email' , 'gender' , 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['phone_number'] , validated_data['email'] , validated_data['gender'] , validated_data['password'])
        return user