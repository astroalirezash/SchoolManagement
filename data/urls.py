from django.urls import path

from .views import (
    RcardView
)


app_name = 'data'

urlpatterns = [
    path('report-card', RcardView.as_view(), name='rcard')
]
