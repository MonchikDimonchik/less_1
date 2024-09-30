from django.urls import path
from tmp.views import index, catalog

urlpatterns = [
    path('', index),
    path('catalog/', catalog),
]