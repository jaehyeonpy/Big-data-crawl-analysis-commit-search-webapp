from django.urls import include, path


urlpatterns = [
    path(
        'crawl-analysis-commit-er/', 
        include('crawl-analysis-commit-er.urls')
        ),
    path(
        'searcher/', 
        include('searcher.urls')
        ),
]