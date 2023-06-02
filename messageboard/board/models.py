from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Announce(models.Model):
    # Tanks, Healers, DD, Merchants, Guild Masters, Quest Givers, Blacksmiths, Tanners, Potion Makers, Spell Masters
    # Танки, Хилы, ДД, Торговцы, Гилдмастеры, Квестгиверы, Кузнецы, Кожевники, Зельевары, Мастера заклинаний
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Текс объявления')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время редактирования')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категории')

    # reply = models.ForeignKey('Reply', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse('post', kwargs={'post_id': self.pk})
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['time_create', 'title']


class Reply(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    content = models.TextField(blank=True, verbose_name='Ответ')
    is_acceptable = models.BooleanField(default=False, verbose_name='Принято')
    announce = models.ForeignKey(Announce, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('reply', kwargs={'rep_id': self.pk})

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('category', kwargs={'cat_id': self.pk})
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']
