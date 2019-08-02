from django.db import models
from django.conf import settings
import uuid
# Create your models here.
from django.contrib.auth.models import User, Group


class Video(models.Model):
    key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    file_1080p = models.CharField(max_length=255, null=True)
    file_720p = models.CharField(max_length=255, null=True
                                 )
    file_watermark = models.CharField(max_length=255, null=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def upload_video_dir(self, filename):
        path = '{}/{}'.format(self.key, "video_original.mp4")
        return path
    file = models.FileField(upload_to=upload_video_dir)


