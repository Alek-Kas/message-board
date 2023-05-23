from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import Announce

# menu = ['О сайте', 'Добавить объявление', 'Поиск своих объявлений', 'Войти']
menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить объявление', 'url_name': 'add_announce'},
    {'title': 'Поиск своих объявлений', 'url_name': 'find_announce'},
    {'title': 'Войти', 'url_name': 'login'},
]

cats = [
    (TANKS, 'Танки'),
    (HEALERS, 'Хилы'),
    (DD, 'ДД'),
    (MERCHANTS, 'Торговцы'),
    (GUILD_MASTERS, 'Гилдмастеры'),
    (QUEST_GIVERS, 'Квестгиверы'),
    (BLACKSMITHS, 'Кузнецы'),
    (TANNERS, 'Кожевники'),
    (POTION_MAKERS, 'Зельевары'),
    (SPELL_MASTERS, 'Мастера заклинаний'),
]

def index(request):
    posts = Announce.objects.all()
    # cats = Announce.categories.all()

    context = {
        'posts': posts,
        # 'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'board/index.html', context=context)


def about(request):
    return render(request, 'board/about.html', {'menu': menu, 'title': 'О сайте'})


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
    return HttpResponse(f'Отображение категории с id = {cat_id}')


