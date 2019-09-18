import os
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

class Guide(models.Model):
  title = models.CharField(max_length=250)
  description = models.TextField(blank=True, null=True)
  added_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
  guide_file = models.FileField(upload_to='guides/')
  template = models.FileField(upload_to='templates/', blank=True, null=True)

  def __str__(self):
    return self.title

  def delete(self, *args, **kwargs):
        self.template.delete()
        super(Guide, self).delete(*args, **kwargs)


# These two auto-delete files from filesystem when they are unneeded:
@receiver(models.signals.post_delete, sender=Guide)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Guide` object is deleted.
    """
    if instance.template:
        if os.path.isfile(instance.template.path):
            os.remove(instance.template.path)
  
@receiver(models.signals.pre_save, sender=Guide)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `Guide` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_template = Guide.objects.get(pk=instance.pk).template
    except Guide.DoesNotExist:
        return False

    new_template = instance.template
    if not old_template == new_template:
        if os.path.isfile(old_template.path):
            os.remove(old_template.path)