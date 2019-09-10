from django.contrib import admin
from .models import Meeting

class MeetingAdmin(admin.ModelAdmin):
  list_display = ('id', 'subject', 'owner', 'date')
  list_display_links = ('id', 'subject')
  list_per_page = 25

admin.site.register(Meeting, MeetingAdmin)
