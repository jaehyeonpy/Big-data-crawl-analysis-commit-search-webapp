from django.urls import path

from .views import *


app_name = 'db_view'

urlpatterns = [
    path(
        'main/', 
        main, 
        name='main'),
    path(
        'search/', 
        search, 
        name='search'),
]