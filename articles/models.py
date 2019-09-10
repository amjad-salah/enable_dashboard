from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Article(models.Model):
  writer = models.ForeignKey(User, on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=200)
  body = RichTextField()
  created_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title
