from django.conf.urls import url
from django.urls import path

from dyplomowanie.Kontroler.views import hello_world
from dyplomowanie.Kontroler.views import current_datetime
from dyplomowanie.Kontroler.views import hours_ahead

urlpatterns = [
    url('time/plus/(\d{1,2})\$', hours_ahead),
    path('time', current_datetime),
    path('', hello_world)
]