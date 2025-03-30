from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_published', 'views_count')
    list_editable = ('is_published',)
    list_filter = ('title','is_published', 'created_at')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'
