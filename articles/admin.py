from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'writer', 'created_date', 'publish')
  list_display_links = ('id', 'title')
  list_filter = ('writer__first_name',)
  list_editable = ('publish',)
  search_fields = ('title', 'writer__first_name')
  list_per_page = 25

admin.site.register(Article, ArticleAdmin)
