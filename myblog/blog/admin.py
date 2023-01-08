from django.contrib import admin
from .models import PostBlog

@admin.register(PostBlog)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

