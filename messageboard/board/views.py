from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView

from .forms import AddPostForm
from .models import Announce, Category
from .utils import *

# menu = [
#     {'title': 'О сайте', 'url_name': 'about'},
#     {'title': 'Добавить объявление', 'url_name': 'add_announce'},
#     {'title': 'Поиск своих объявлений', 'url_name': 'find_announce'},
#     {'title': 'Войти', 'url_name': 'login'},
# ]


class BoardHome(DataMixin, ListView):
    model = Announce
    template_name = 'board/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # получаем контекст уже существующий
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))


def about(request):
    return render(request, 'board/about.html', {'menu': menu, 'title': 'О сайте'})


class AddAnnounce(DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'board/addpage.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # получаем контекст уже существующий
        c_def = self.get_user_context(title='Добавление объявления')
        return dict(list(context.items()) + list(c_def.items()))


# def add_announce(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(request, 'board/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление объявления'})


def find_announce(request):
    return HttpResponse('Найти объявления')


def login(request):
    return HttpResponse('Добавление объявления')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class ShowPost(DataMixin, DetailView):
    model = Announce
    template_name = 'board/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'  # сюда помещаются данные взятые из Announce

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # получаем контекст уже существующий
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class AnnounceCategory(DataMixin, ListView):
    model = Announce
    template_name = 'board/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Announce.objects.filter(cat__slug=self.kwargs['cat_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # получаем контекст уже существующий
        c_def = self.get_user_context(
            title='Категория - ' + str(context['posts'][0].cat),
            cat_selected=context['posts'][0].cat_id
        )
        return dict(list(context.items()) + list(c_def.items()))
