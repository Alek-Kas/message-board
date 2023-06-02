from django.urls import path, re_path

from .views import *

urlpatterns = [
    # path('', index, name='home'),
    path('', BoardHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('add_announce/', AddAnnounce.as_view(), name='add_announce'),
    path('find_announce/', find_announce, name='find_announce'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    # path('category/<int:cat_id>/', show_category, name='category'),
    path('category/<slug:cat_slug>/', AnnounceCategory.as_view(), name='category'),
]
