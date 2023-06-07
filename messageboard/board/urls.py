from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', BoardHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('add_announce/', AddAnnounce.as_view(), name='add_announce'),
    path('find_announce/', find_announce, name='find_announce'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', AnnounceCategory.as_view(), name='category'),
]
