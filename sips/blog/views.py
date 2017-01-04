from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.views.generic.list import ListView

from blog.models import Blog


def blog_view(request):
    posts = Blog.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


class CreateEntryView(CreateView):
    model = Blog
    fields = '__all__'
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('listado_entries')


class EntryListView(ListView):
    model = Blog
    paginate_by = 50
    template_name = 'blog/listado_blog.html'

    def get_queryset(self):
        return Blog.objects.all().order_by('-id')


class EditEntryView(UpdateView):
    model = Blog
    fields = '__all__'
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('listado_entries')