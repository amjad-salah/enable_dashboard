from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    path('meetings/', include('meetings.urls')),
    path('articles/', include('articles.urls')),
    path('announcements/', include('announcements.urls')),
    path('admin/', admin.site.urls),
]
