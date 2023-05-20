from django.urls import path, re_path

from .views import index, announcement, archive, about

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),

    # path('announce/<int:ann_id>', announcement),
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive)
]
