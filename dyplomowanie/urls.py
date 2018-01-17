from django.urls import path

from dyplomowanie.kontroler.views import Base
from dyplomowanie.kontroler.views import Topics

urlpatterns = [
    path('index', Base.as_view(), name = "base"),
    path('przegladanie_list', Topics.as_view(), name = "topics")
]
