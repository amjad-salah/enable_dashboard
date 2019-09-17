from django.contrib import admin
from .models import Mission

class MissionAdmin(admin.ModelAdmin):
  list_display = ('id', 'subject', 'from_date', 'to_date')
  list_display_links = ('id', 'subject')
  list_per_page = 25


admin.site.register(Mission, MissionAdmin)
