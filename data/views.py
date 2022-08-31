from urllib import request
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import (
    ReportCard
)

# Create your views here.


# class ReportCardListView(ListView): TODO: ReportCard List View
#     userid = request.user.id
#     model = ReportCard
#     queryset = ReportCard.objects.filter(student_id=userid)
#     template_name = ''


class ReportCardDetailView(LoginRequiredMixin, DetailView):
    def get_object(self):
        rcard_year = self.kwargs.get('year')
        user = self.request.user.id
        rcard = get_object_or_404(ReportCard, student_id=user, year=rcard_year)
        return rcard
    template_name = 'data/ReportCard.html'
    context_object_name = 'rcard'
    
