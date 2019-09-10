from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Meeting(models.Model):
  owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
  subject = models.CharField(max_length=200)
  agenda = RichTextField()
  date = models.DateTimeField()
  finished = models.BooleanField(default=False)

  def __str__(self):
    return self.subject

