from django.urls import path

from .views import (
    NewsDetailView
)

app_name = 'content'

urlpatterns = [
    path('news/<pk>', NewsDetailView.as_view(), name='snews')
]


