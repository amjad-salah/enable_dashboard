from django.contrib import admin
from django.contrib.auth.models import User
from .models import Article, Comment

class ArticleAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'writer', 'created_date', 'publish')
  list_display_links = ('id', 'title')
  list_filter = ('writer__first_name',)
  list_editable = ('publish',)
  search_fields = ('title', 'writer__first_name')
  list_per_page = 25

  # Populate writer with default logged in user in admin site 
  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    if db_field.name == 'writer':
        kwargs['queryset'] = User.objects.filter(username=request.user)
    return super(ArticleAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

  def get_readonly_fields(self, request, obj=None):
    if obj is not None:
        return self.readonly_fields + ('writer',)
    return self.readonly_fields

  def add_view(self, request, form_url="", extra_context=None):
    data = request.GET.copy()
    data['writer'] = request.user
    request.GET = data
    return super(ArticleAdmin, self).add_view(request, form_url="", extra_context=extra_context)

admin.site.register(Article, ArticleAdmin)

class CommentAdmin(admin.ModelAdmin):
  list_display = ('id', 'user', 'articl', 'created_date')
  list_filter = ('user__first_name',)
  list_per_page = 25

admin.site.register(Comment, CommentAdmin)