from django.shortcuts import render
from news.models import News
from project.models import Project
from researcher.models import Researcher
# Create your views here.

def index(request):
    news = News.objects.order_by('-date')
    if len(news) > 20:
        news = news[:20]
    projects = Project.objects.order_by('-start_date')
    context = {
        'news': news,
        'projects': projects
    }
    return render(request, 'pages/index.html', context)

def about(request):
    members = Researcher.objects.order_by('last_name', 'name')
    unactives = members.filter(active = False)
    directors = members.filter(position = 'DIR').filter(active = True)
    subdirectors = members.filter(position = 'SUBDIR').filter(active = True)
    investigators = members.filter(position = 'INV').filter(active = True)
    ug_thesists = members.filter(position = 'TH_UG').filter(active = True)
    pg_thesists = members.filter(position = 'TH_PG').filter(active = True)
    phd_thesists = members.filter(position = 'TH_PHD').filter(active = True)
    colaborators = members.filter(position = 'COLAB').filter(active = True)
    context = {
        'directors': directors,
        'subdirectors': subdirectors,
        'investigators': investigators,
        'ug': ug_thesists,
        'pg': pg_thesists,
        'phd': phd_thesists,
        'colaborators': colaborators,
        'unactives': unactives,
    }
    return render(request, 'pages/about.html', context)
