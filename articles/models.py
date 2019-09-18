import os
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.dispatch import receiver

class Article(models.Model):
  writer = models.ForeignKey(User, on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=200)
  body = RichTextUploadingField()
  created_date = models.DateTimeField(auto_now_add=True)
  attachment = models.FileField(upload_to='articles/', blank=True, null=True)
  publish = models.BooleanField(default=False)

  def __str__(self):
    return self.title

  def delete(self, *args, **kwargs):
        self.attachment.delete()
        super(Article, self).delete(*args, **kwargs)

# These two auto-delete files from filesystem when they are unneeded:
@receiver(models.signals.post_delete, sender=Article)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Article` object is deleted.
    """
    if instance.attachment:
        if os.path.isfile(instance.attachment.path):
            os.remove(instance.attachment.path)

class Comment(models.Model):
  articl = models.ForeignKey(Article, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  body = models.TextField()
  created_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.body[:25]
