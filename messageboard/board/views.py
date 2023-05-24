from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import Announce

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить объявление', 'url_name': 'add_announce'},
    {'title': 'Поиск своих объявлений', 'url_name': 'find_announce'},
    {'title': 'Войти', 'url_name': 'login'},
]

cats = [
    {'title': 'Танки', 'url_name': 'tanks'},
    {'title': 'Хилы', 'url_name': 'healers'},
    {'title': 'ДД', 'url_name': 'dd'},
    {'title': 'Гилдмастеры', 'url_name': 'guild_masters'},
    {'title': 'Квестгиверы', 'url_name': 'quest_givers'},
    {'title': 'Кузнецы', 'url_name': 'blacksmiths'},
    {'title': 'Кожевники', 'url_name': 'tanners'},
    {'title': 'Зельевары', 'url_name': 'potion_makers'},
    {'title': 'Мастера заклинаний', 'url_name': 'spell_masters'},
    {'title': 'Торговцы', 'url_name': 'merchants'},
]


def index(request):
    posts = Announce.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'board/index.html', context=context)


def about(request):
    return render(request, 'board/about.html', {'menu': menu, 'cats': cats, 'title': 'О сайте'})


def add_announce(request):
    return HttpResponse('Добавление объявления')


def find_announce(request):
    return HttpResponse('Добавление объявления')


def login(request):
    return HttpResponse('Добавление объявления')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_post(request, post_id):
    return HttpResponse(f'Отображение объявления с id = {post_id}')


def show_category(request, cat_id):
    posts = Announce.objects.filter(cat_id=cat_id)
    if len(posts) == 0:
        raise Http404()
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }
    return render(request, 'board/index.html', context=context)
