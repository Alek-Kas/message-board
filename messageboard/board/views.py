from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Страница приложения board')


def announcement(request):
    return HttpResponse('<h1>Объявления по категориям</h1>')
