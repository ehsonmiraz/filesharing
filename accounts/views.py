from rest_framework import generics,permissions
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import send_mail
from .serializers import UserSerializer
from cryptography.fernet import Fernet
import os

User = get_user_model()

# Define a key for URL encryption
# ENCRYPTION_KEY = '0BwXAFSPjpv02_MprYrVcG3L9LoY2K4TGM-N4VwHv0I='
# bytes(ENCRYPTION_KEY, encoding='utf8')
# print(ENCRYPTION_KEY)
# cipher_suite = Fernet(ENCRYPTION_KEY.encode())

class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    def perform_create(self, serializer):
        user = serializer.save()
        token = RefreshToken.for_user(user)
        verification_url = f"http://yourdomain.com/verify-email/?token={token}"
        
        send_mail(
            'Verify your email',
            f'Click the link to verify your email: {verification_url}',
            'from@example.com',
            [user.email],
        )
