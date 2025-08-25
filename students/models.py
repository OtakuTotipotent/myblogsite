import os
from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to="profiles/", blank=True, null=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        if self.profile_pic:
            if os.path.isfile(self.profile_pic.path):
                os.remove(self.profile_pic.path)
        super().delete(*args, **kwargs)
