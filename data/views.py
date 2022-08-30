from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import Http404

from .models import (
    ReportCard
)
from account.models import User

# Create your views here.


class RcardView(LoginRequiredMixin, View):

    def get(self, request):
        user = request.user.id
        rcard = get_object_or_404(ReportCard, student_id=user)
        context = {
            'rcard': rcard
        }
        return render(request, 'data/ReportCard.html', context)            
