from django.urls import path

from .views import *


app_name = 'crawl-analysis-commit-er'

urlpatterns = [
    path(
        '', 
        main, 
        name='main'),
    path(
        'crawler-analyzer', 
        crawler_analyzer, 
        name='crawler_analyzer'),
    path(
        'committer', 
        committer, 
        name='committer'), 
]