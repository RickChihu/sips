from django.shortcuts import render
from blog.models import Blog


def blog_view(request):
    posts = Blog.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})