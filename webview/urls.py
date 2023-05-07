from django.urls import include, path


urlpatterns = [
    path(
        'crawled_view/', 
        include('crawled_view.urls')),
    path(
        'db_view/', 
        include('db_view.urls')),
]