from django.db import models
from django.conf import settings
# Create your models here.
class File(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
