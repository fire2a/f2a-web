from django.shortcuts import render
from news.models import News
from project.models import Project
from researcher.models import Researcher
# Create your views here.

def index(request):
    news = News.objects.order_by('-date')
    if len(news) > 5:
        news = news[:5]
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
    principal_investigators = members.filter(position = 'INV_P').filter(active = True)
    assoc_investigators = members.filter(position = 'INV_A').filter(active = True)
    foreign_investigators = members.filter(position = 'INV_E').filter(active = True)
    colab_investigators = members.filter(position = 'INV_C').filter(active = True)
    ug_thesists = members.filter(position = 'TH_UG').filter(active = True)
    pg_thesists = members.filter(position = 'TH_PG').filter(active = True)
    phd_thesists = members.filter(position = 'TH_PHD').filter(active = True)
    context = {
        'directors': directors,
        'subdirectors': subdirectors,
        'principal_investigators': principal_investigators,
        'assoc_investigators': assoc_investigators,
        'foreign_investigators': foreign_investigators,
        'colab_investigators': colab_investigators,
        'ug': ug_thesists,
        'pg': pg_thesists,
        'phd': phd_thesists,
        'unactives': unactives,
    }
    return render(request, 'pages/about.html', context)
