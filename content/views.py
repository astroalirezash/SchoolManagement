from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import News

# Create your views here.


class NewsDetailView(DetailView):
    model = News
    template_name = "content/News.html"
    context_object_name = 'news'


class NewsListView(ListView):
    model = News
    queryset = News.objects.all().order_by('date_added')
    context_object_name = 'news'
    template_name = 'content/NewsList.html'
