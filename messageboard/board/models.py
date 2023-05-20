from django.contrib.auth.models import User
from django.db import models


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
        (GUILD_MASTERS, 'Гилдмастеры'),
        (QUEST_GIVERS, 'Квестгиверы'),
        (BLACKSMITHS, 'Кузнецы'),
        (TANNERS, 'Кожевники'),
        (POTION_MAKERS, 'Зельевары'),
        (SPELL_MASTERS, 'Мастера заклинаний'),
    ]
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_created=True)
    time_update = models.DateTimeField(auto_now=True)
    categories = models.CharField(max_length=2, choices=CATEGORIES_CHOICES)


class Reply(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    acceptable = models.BooleanField(bool=False)
    announce = models.ForeignKey(Announce, on_delete=models.CASCADE)
