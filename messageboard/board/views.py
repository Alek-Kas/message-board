from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView

from .forms import AddPostForm
from .models import Announce, Category

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить объявление', 'url_name': 'add_announce'},
    {'title': 'Поиск своих объявлений', 'url_name': 'find_announce'},
    {'title': 'Войти', 'url_name': 'login'},
]


class BoardHome(ListView):
    model = Announce
    template_name = 'board/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # получаем контекст уже существующий
        context['menu'] = menu  # добавляем к нему меню из списка выше
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context


def about(request):
    return render(request, 'board/about.html', {'menu': menu, 'title': 'О сайте'})


class AddAnnounce(CreateView):
    form_class = AddPostForm
    template_name = 'board/addpage.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # получаем контекст уже существующий
        context['menu'] = menu  # добавляем к нему меню из списка выше
        context['title'] = 'Добавление объявления'
        return context


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


class ShowPost(DetailView):
    model = Announce
    template_name = 'board/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'  # сюда помещаются данные взятые из Announce

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # получаем контекст уже существующий
        context['menu'] = menu  # добавляем к нему меню из списка выше
        context['title'] = str(context['object'])
        # context['cat_selected'] = context['posts'][0].cat_id
        return context


# def show_post(request, post_slug):
#     post = get_object_or_404(Announce, slug=post_slug)
#     context = {
#         'post': post,
#         'menu': menu,
#         'cat_selected': post.cat_id,
#     }
#     return render(request, 'board/post.html', context=context)


class AnnounceCategory(ListView):
    model = Announce
    template_name = 'board/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Announce.objects.filter(cat__slug=self.kwargs['cat_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # получаем контекст уже существующий
        context['menu'] = menu  # добавляем к нему меню из списка выше
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context
