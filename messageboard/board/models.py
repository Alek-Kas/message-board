from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Announce(models.Model):
    # Tanks, Healers, DD, Merchants, Guild Masters, Quest Givers, Blacksmiths, Tanners, Potion Makers, Spell Masters
    # Танки, Хилы, ДД, Торговцы, Гилдмастеры, Квестгиверы, Кузнецы, Кожевники, Зельевары, Мастера заклинаний
    TANKS = 'TK'
    HEALERS = 'HL'
    DD = 'DD'
    MERCHANTS = 'MR'
    GUILD_MASTERS = 'GM'
    QUEST_GIVERS = 'QG'
    BLACKSMITHS = 'BS'
    TANNERS = 'TN'
    POTION_MAKERS = 'PM'
    SPELL_MASTERS = 'SM'
    CATEGORIES_CHOICES = [
        (TANKS, 'Танки'),
        (HEALERS, 'Хилы'),
        (DD, 'ДД'),
        (MERCHANTS, 'Торговцы'),
        (GUILD_MASTERS, 'Гилдмастера'),
        (QUEST_GIVERS, 'Квестгиверы'),
        (BLACKSMITHS, 'Кузнецы'),
        (TANNERS, 'Кожевники'),
        (POTION_MAKERS, 'Зельевары'),
        (SPELL_MASTERS, 'Мастера заклинаний'),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    categories = models.CharField(max_length=2, choices=CATEGORIES_CHOICES)
    # reply = models.ForeignKey('Reply', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse('post', kwargs={'post_id': self.pk})
        return reverse('post', kwargs={'post_id': self.pk, 'cat_id': self.categories})


class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    is_acceptable = models.BooleanField(default=False)
    announce = models.ForeignKey(Announce, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('reply', kwargs={'rep_id': self.pk})
