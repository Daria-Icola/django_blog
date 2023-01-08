from django.shortcuts import render
from django.views.generic.base import View
from .models import PostBlog

class PostView(View):
    def get(self, request):
        posts = PostBlog.objects.all()
        return render(request, 'blog/blog.html', {'post_list': posts})

