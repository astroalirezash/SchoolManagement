from django.shortcuts import render
from django.views.generic import DetailView

from .models import News

# Create your views here.


class NewsDetailView(DetailView):
    model = News
    template_name = "content/News.html"
    context_object_name = 'news'
