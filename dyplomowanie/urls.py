from django.urls import path

from dyplomowanie.kontroler.views import Base
from dyplomowanie.kontroler.views import Topics
from dyplomowanie.kontroler.views import Topics_Options
from dyplomowanie.kontroler.views import Work
from dyplomowanie.kontroler.views import Declaration

urlpatterns = [
    path('index', Base.as_view(), name = "base"),
    path('tematy/przegladaj', Topics.as_view(), name = "topics"),
    path('tematy', Topics_Options.as_view(), name = "topics_options"),
    path('moja_praca/deklaracja', Declaration.as_view(), name = "declaration"),
    path('moja_praca', Work.as_view(), name = "work"),
    path('', Base.as_view(), name = "base")
]
