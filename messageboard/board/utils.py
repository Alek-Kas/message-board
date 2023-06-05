from .models import Category

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить объявление', 'url_name': 'add_announce'},
    {'title': 'Поиск своих объявлений', 'url_name': 'find_announce'},
    {'title': 'Войти', 'url_name': 'login'},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['menu'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
