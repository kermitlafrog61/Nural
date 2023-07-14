from django.http import HttpResponseRedirect
from django.shortcuts import render

from apps.news.models import News


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
    }
    return render(request, 'index.html', context)
