from django.db import models
from django.conf import settings
import uuid
# Create your models here.
from django.contrib.auth.models import User, Group, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates And Saves A New User"""

        user = get_user_model()
        user.model(email=email, **extra_fields)  # type:
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'email'


class Video(models.Model):
    key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    file_1080p = models.CharField(max_length=255, null=True)
    file_720p = models.CharField(max_length=255, null=True
                                 )
    file_watermark = models.CharField(max_length=255, null=True)

    def upload_video_dir(self, filename):
        path = '{}/{}'.format(self.key, "video_original.mp4")
        return path

    file = models.FileField(upload_to=upload_video_dir)
