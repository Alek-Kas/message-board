from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AddPostForm
from .models import Announce, Category

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить объявление', 'url_name': 'add_announce'},
    {'title': 'Поиск своих объявлений', 'url_name': 'find_announce'},
    {'title': 'Войти', 'url_name': 'login'},
]


def index(request):
    posts = Announce.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'board/index.html', context=context)


def about(request):
    return render(request, 'board/about.html', {'menu': menu, 'title': 'О сайте'})


def add_announce(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'board/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление объявления'})


def find_announce(request):
    return HttpResponse('Найти объявления')


def login(request):
    return HttpResponse('Добавление объявления')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_post(request, post_slug):
    post = get_object_or_404(Announce, slug=post_slug)
    context = {
        'post': post,
        'menu': menu,
        'cat_selected': post.cat_id,
    }
    return render(request, 'board/post.html', context=context)


def show_category(request, cat_id):
    posts = Announce.objects.filter(cat_id=cat_id)
    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }

    return render(request, 'board/index.html', context=context)
