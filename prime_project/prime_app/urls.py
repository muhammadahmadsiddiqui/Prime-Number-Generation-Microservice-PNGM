from django.urls import path
from . import services

urlpatterns = [
    path('generate/', services.generate, name='generate'),
    path('monitor/', services.monitor, name='monitor'),
    path('get/', services.get, name='get'),
]
