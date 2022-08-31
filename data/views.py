from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import (
    ReportCard
)

# Create your views here.


class ReportCards(LoginRequiredMixin, View):
    def get(self, request):
        userid = request.user.id
        rcards = ReportCard.objects.filter(student_id=userid)
        context = {
            'rcards': rcards
        }
        return render(request, 'data/ReportCards.html', context)


class ReportCardDetailView(LoginRequiredMixin, DetailView):
    def get_object(self):
        rcard_year = self.kwargs.get('year')
        user = self.request.user.id
        rcard = get_object_or_404(ReportCard, student_id=user, year=rcard_year)
        return rcard
    template_name = 'data/ReportCard.html'
    context_object_name = 'rcard'
    
