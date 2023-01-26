from django.shortcuts import render, get_object_or_404
from .models import News

# Create your views here.
def index(request):
    news = News.objects.order_by('-date')
    featured = news.filter(featured=True)
    if len(news) > 20:
        news = news[:20]
    context = {
        'news': news,
        'featured': featured,
    }
    return render(request, 'news/news.html', context)

def new(request, new_id):
    new = get_object_or_404(News, pk = new_id)
    context = {
        'new': new
    }
    return render(request, 'news/new.html', context)