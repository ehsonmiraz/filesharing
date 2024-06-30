from rest_framework import serializers
from .models import File
from .validators import validate_file_extension
class FileSerializer(serializers.ModelSerializer):
    file = serializers.FileField(validators=[validate_file_extension])
    class Meta:
        model = File
        fields = ('id', 'file', 'uploaded_by', 'uploaded_at')
        read_only_fields = ['uploaded_by']