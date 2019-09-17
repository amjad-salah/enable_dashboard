from django.db import models
from ckeditor.fields import RichTextField

class Mission(models.Model):
  subject = models.CharField(max_length=250)
  participants = models.TextField()
  objectives = RichTextField()
  recommendations = RichTextField(blank=True, null=True)
  from_date = models.DateTimeField()
  to_date = models.DateTimeField()

  def __str__(self):
    return self.subject
