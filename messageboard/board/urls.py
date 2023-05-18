from django.urls import path

from .views import index, announcement

urlpatterns = [
    path('', index),
    path('announce/', announcement),
]