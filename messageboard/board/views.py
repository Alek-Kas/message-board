from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import AddPostForm, RegisterUserForm, LoginUserForm
from .models import Announce, Category
from .utils import *


class BoardHome(DataMixin, ListView):
    model = Announce
    template_name = 'board/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # получаем контекст уже существующий
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Announce.objects.all().select_related('cat')


def about(request):
    return render(request, 'board/about.html', {'menu': menu, 'title': 'О сайте'})


class AddAnnounce(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'board/addpage.html'
    success_url = reverse_lazy('home')  # Переадресация для зарегистрированных
    login_url = reverse_lazy('home')  # Переадресация для не зарегистрированных
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # получаем контекст уже существующий
        c_def = self.get_user_context(title='Добавление объявления')
        return dict(list(context.items()) + list(c_def.items()))


def find_announce(request):
    return HttpResponse('Найти объявления')


# def login(request):
#     return HttpResponse('Добавление объявления')


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
        return Announce.objects.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # получаем контекст уже существующий
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(
            title='Категория - ' + str(c.name),
            cat_selected=c.pk
        )
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    # form_class = UserCreationForm
    form_class = RegisterUserForm
    template_name = 'board/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # получаем контекст уже существующий
        c_def = self.get_user_context(
            title='Регистрация'
        )
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'board/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
