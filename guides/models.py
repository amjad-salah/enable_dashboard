from django.db import models
from django.contrib.auth.models import User

class Guide(models.Model):
  title = models.CharField(max_length=250)
  description: models.TextField()
  added_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
  template = models.FileField(upload_to='guides/')

  def __str__(self):
    return self.title

  