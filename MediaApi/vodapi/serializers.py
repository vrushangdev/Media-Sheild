from django.contrib.auth.models import User, Group
from .models import Video
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # videos = VideoSerializer(read_only=True, many=True)
    # print(videos)

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'first_name', 'last_name', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ('file', 'name', 'uploaded_by')
