from django.urls import path
from .views import *

app_name = 'places'

urlpatterns = [
    path('', places, name='places-list')
]
