from django.contrib import admin
from .models import Announcement

class AnnouncementAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'created_date')
  list_display_links = ('id', 'title')
  list_per_page = 25

admin.site.register(Announcement, AnnouncementAdmin)
