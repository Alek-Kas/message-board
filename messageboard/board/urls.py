from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('add_announce/', add_announce, name='add_announce'),
    path('find_announce/', find_announce, name='find_announce'),
    path('login/', login, name='login'),
    path('post/<int:post_id/', show_post, name='post'),
    path('post/<str:cat_id/', show_category, name='category'),
]
