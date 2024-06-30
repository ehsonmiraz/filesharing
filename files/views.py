
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action,permission_classes
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from cryptography.fernet import Fernet
import base64
import os
from .models import File
from .serializers import FileSerializer
from .permissions import IsOpsUser,IsClientUser
from django.conf import settings  
from .encryption_util import encrypt,decrypt




class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes=[permissions.IsAuthenticated]


    def list(self, request, *args, **kwargs):
        if(not self.request.user.is_client_user):
            return  Response({"error": "You do not have permission to list files."}, status=status.HTTP_403_FORBIDDEN)
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def perform_create(self, serializer):
        if(not self.request.user.is_ops_user):
            return  Response({"error": "You do not have permission to upload files."}, status=status.HTTP_403_FORBIDDEN)
        serializer.save(uploaded_by=self.request.user)
   
            
    
    @action(detail=True, methods=['get'], permission_classes=[permissions.IsAuthenticated,IsClientUser])
    def download_link(self, request, pk=None):
        encrypted_url = f"http://{settings.DOMAIN}/api/files/{encrypt(pk)}/download/"
        return Response({
                "download-link": encrypted_url,
                "message": "success"
        })
       
    @action(detail=True, methods=['get'], permission_classes=[permissions.IsAuthenticated,IsClientUser])
    def download(self, request, pk=None):
        pk=decrypt(pk) 
        try:
            file_instance = get_object_or_404(File, pk=pk)
            if file_instance:
                response = FileResponse(file_instance.file.open(), as_attachment=True)
                return response
            else:
                return Response({"error": "Invalid download URL."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

