from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'file', 'uploaded_by', 'uploaded_at')
        read_only_fields = ['uploaded_by']