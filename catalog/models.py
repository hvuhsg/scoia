from django.db import models
from django.urls import reverse
from django.conf import settings
import os


def get_image_path(instance, filename):
    path = instance.photo_path()
    return path


class Photo(models.Model):
    profile_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    title = models.CharField(max_length=200)
    summary = models.TextField(
        max_length=300, help_text="Enter a brief description of the photo"
    )

    def create_filename(self):
        self.filename = self.title + "." + self.profile_image.name.split(".")[-1]
        return self.filename

    def photo_path(self):
        res = self.create_filename()
        return res

    def __str__(self):
        """String for representing the Model object."""
        return self.title
