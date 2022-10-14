from rest_framework import serializers
from .models import VideoDatabase

class YoutubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoDatabase
        fields = "__all__"