from django.urls import path

from .views import *


app_name = 'searcher'

urlpatterns = [
    path(
        '', 
        main, 
        name='main'),
]