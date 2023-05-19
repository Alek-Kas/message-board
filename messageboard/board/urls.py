from django.urls import path, re_path

from .views import index, announcement, archive

urlpatterns = [
    path('', index, name='home'),
    path('announce/<int:ann_id>', announcement),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive)
]
