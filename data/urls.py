from django.urls import path

from .views import (
    ReportCardDetailView,
    ReportCards
)


app_name = 'data'

urlpatterns = [
    path('report-card', ReportCards.as_view(), name='rcards'),
    path('report-card/<str:year>', ReportCardDetailView.as_view(), name='rcard_detail')
]
