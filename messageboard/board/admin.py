from django.contrib import admin

from .models import *


class AnnounceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'author')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('time_create',)
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class ReplyAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'author', 'is_acceptable')
    list_display_links = ('id', 'content')
    search_fields = ('content', 'author', 'is_acceptable')
    prepopulated_fields = {'slug': ('content',)}


admin.site.register(Announce, AnnounceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Reply, ReplyAdmin)
