from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404, render

from . import models
from .forms import CommentForm

class ArticleListView(ListView):
    model = models.Article
    template_name = 'article_list.html'
    fields = ['title', 'body', 'cover', 'author']
    def home_page(request):
        if request.method == 'POST' and request.FILES:
                # получаем загруженный файл
            file = request.FILES['myfile1']
            fs = FileSystemStorage()
                # сохраняем на файловой системе
            filename = fs.save(file.name, file)
                # получение адреса по которому лежит файл
            file_url = fs.url(filename)
            return render(request, 'home_page.html', {
                    'file_url': file_url
            })
        return render(request, 'article_list.html')

class ArticleDetailView(DetailView):
    model = models.Article
    template_name = 'article_detail.html'

class ArticleUpdateView(UpdateView):
    model = models.Article
    fields = ['title', 'body', 'cover']
    template_name = 'article_edit.html'
    def home_page(request):
        if request.method == 'POST' and request.FILES:
            # получаем загруженный файл
            file = request.FILES['myfile1']
            fs = FileSystemStorage()
            # сохраняем на файловой системе
            filename = fs.save(file.name, file)
            # получение адреса по которому лежит файл
            file_url = fs.url(filename)
            return render(request, 'home_page.html', {
                'file_url': file_url
            })
        return render(request, 'article_edit.html')

class ArticleDeleteView(DeleteView):
    model = models.Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

class ArticleCreateView(CreateView):
    model = models.Article
    template_name = 'article_new.html'
    fields = ['title', 'body', 'cover', 'author']
    def home_page(request):
        if request.method == 'POST' and request.FILES:
                # получаем загруженный файл
            file = request.FILES['myfile1']
            fs = FileSystemStorage()
                # сохраняем на файловой системе
            filename = fs.save(file.name, file)
                # получение адреса по которому лежит файл
            file_url = fs.url(filename)
            return render(request, 'home_page.html', {
                    'file_url': file_url
            })
        return render(request, 'article_new.html')
