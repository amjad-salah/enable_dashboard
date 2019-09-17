from django.contrib import admin
from .models import Guide

class GuideAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'added_by')
  list_display_links = ('id', 'title')
  list_per_page = 25
  search_fields = ('title',)


admin.site.register(Guide, GuideAdmin)