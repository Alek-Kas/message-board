from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import Announce

menu = ['О сайте', 'Добавить объявление', 'Поиск своих объявлений', 'Войти']


def index(request):
    posts = Announce.objects.all()
    return render(request, 'board/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'board/about.html', {'menu': menu, 'title': 'О сайте'})


def announcement(request, ann_id):
    return HttpResponse(f'<h1>Объявления по категориям</h1><p>{ann_id}</p>')


def archive(request, year):
    if int(year) > 2023:
        return redirect('home', permanent=True)
        # raise Http404()

    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
