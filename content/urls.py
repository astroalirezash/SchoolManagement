from django.urls import path

from .views import (
    NewsDetailView,
    NewsListView
)

app_name = 'content'

urlpatterns = [
    path('news/<pk>', NewsDetailView.as_view(), name='snews'),  # single news
    path('news', NewsListView.as_view(), name='news')
]


