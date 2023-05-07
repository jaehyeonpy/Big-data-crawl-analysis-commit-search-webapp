from django.urls import path

from .views import *


app_name = 'crawled_view'

urlpatterns = [
    path(
        'main/', 
        main, 
        name='main'),
    path(
        'crawl/', 
        crawl, 
        name='crawl'),
    path(
        'commit/', 
        commit, 
        name='commit'), 
]