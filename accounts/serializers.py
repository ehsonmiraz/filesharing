from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_ops_user', 'is_client_user']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            is_ops_user=validated_data.get('is_ops_user', False),
            is_client_user=validated_data.get('is_client_user', False),
        )
        user.is_active = True  # Ensure the user is active
        user.save()
        return user
