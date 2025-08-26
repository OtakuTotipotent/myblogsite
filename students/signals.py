import os
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from .models import Student


@receiver(pre_save, sender=Student)
def delete_old_profile_pic_on_update(sender, instance, **kwargs):
    # checking if it is an update (rather than a fresh profile creation)
    if not instance.pk:
        return

    try:
        old_pic = Student.objects.get(pk=instance.pk).profile_pic
    except Student.DoesNotExist:
        return

    new_pic = instance.profile_pic
    if old_pic and old_pic != new_pic:
        if os.path.isfile(old_pic.path):
            os.remove(old_pic.path)


@receiver(post_delete, sender=Student)
def delete_profile_pic_on_student_delete(sender, instance, **kwargs):
    if instance.profile_pic:
        if os.path.isfile(instance.profile_pic.path):
            os.remove(instance.profile_pic.path)
