from django.urls import path

from .views import (
    ReportCardDetailView
)


app_name = 'data'

urlpatterns = [
    # TODO: path: report-card
    path('report-card/<str:year>', ReportCardDetailView.as_view(), name='rcard')
]
