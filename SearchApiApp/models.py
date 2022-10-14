from django.db import models

# Create your models here.
class VideoDatabase(models.Model):
    video_id = models.CharField(
        null=False,
        blank=False,
        max_length=200
    )

    title = models.CharField(
        null=True,
        blank=True,
        max_length=500
    )

    description = models.CharField(
        null=True,
        blank=True,
        max_length=5000
    )

    publishing_datetime = models.DateTimeField()

    thumbnail_url = models.URLField()