import os
from django.db import models


def student_profile_upload(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{instance.name.lower().replace(' ', '_')}.{ext}"
    return os.path.join("profiles/", filename)


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(
        upload_to=student_profile_upload, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        if self.profile_pic:
            if os.path.isfile(self.profile_pic.path):
                os.remove(self.profile_pic.path)
        super().delete(*args, **kwargs)
