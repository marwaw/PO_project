from django.conf.urls import url
from django.urls import path

from dyplomowanie.kontroler.views import hello_world
from dyplomowanie.kontroler.views import MojeView
from dyplomowanie.kontroler.views import index

urlpatterns = [
    path('moje', MojeView.as_view(), name='moje'),
    path('index', index),
    path('', hello_world)
]
