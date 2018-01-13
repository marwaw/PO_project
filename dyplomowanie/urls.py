from django.conf.urls import url
from django.urls import path

from dyplomowanie.kontroler.views import hello_world
from dyplomowanie.kontroler.views import current_datetime
from dyplomowanie.kontroler.views import hours_ahead
from dyplomowanie.kontroler.views import MojeView

urlpatterns = [
    url('time/plus/(\d{1,2})\$', hours_ahead),
    path('time', current_datetime),
    path('', hello_world),
    path('moje', MojeView.as_view(), name='moje')

]
