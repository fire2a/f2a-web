from django.shortcuts import render
from news.models import News
from project.models import Project
from researcher.models import Researcher
# Create your views here.

def index(request):
    news = News.objects.order_by('-date')
    if len(news) > 20:
        news = news[:20]
    projects = Project.objects.order_by('-date')
    context = {
        'news': news,
        'projects': projects
    }
    return render(request, 'pages/index.html', context)

def about(request):
    members = Researcher.objects.order_by('last_name', 'name')
    unactives = members.filter(active = False)
    directors = members.filter(position = 'DIR').filter(active = True)
    investigators = members.filter(position = 'INV').filter(active = True)
    postdocs = members.filter(position = 'POST').filter(active = True)
    phds = members.filter(position = 'PHD').filter(active = True)
    masters = members.filter(position = 'MG').filter(active = True)
    undergraduates = members.filter(position = 'PG').filter(active = True)
    context = {
        'directors': directors,
        'investigators': investigators,
        'postdocs': postdocs,
        'phds': phds,
        'masters': masters,
        'undergraduates': undergraduates,
        'unactives': unactives,
    }
    return render(request, 'pages/about.html', context)
