# Generated by Django 4.2.13 on 2024-06-29 13:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UploadedFile',
            new_name='File',
        ),
    ]
