from django.shortcuts import render, get_object_or_404
from .models import Paper
from researcher.models import Researcher
from research.models import Research

# Create your views here.
def index(request):
    papers = Paper.objects.order_by('-date')
    types = {paper.type: paper.get_type_display() for paper in papers}
    researchers = Researcher.objects.all()
    researchs = Research.objects.all()
    authors = {researcher.id: f"{researcher.name} {researcher.last_name}"  for researcher in researchers}
    topics = {topic.id: f"{topic.name}"  for topic in researchs}
    dates = Paper.objects.values_list('date', flat=True).distinct()
    context = {
        'papers': papers,
        'authors': authors,
        'topics': topics,
        'years': [date.year for date in dates],
        'types' : types,
    }
    return render(request, 'papers/papers.html', context)

def search(request):
    papers = Paper.objects.order_by('-date')
    researchers = Researcher.objects.all()
    researchs = Research.objects.all()
    authors = {researcher.id: f"{researcher.name} {researcher.last_name}"  for researcher in researchers}
    topics = {topic.id: f"{topic.name}"  for topic in researchs}
    dates = Paper.objects.values_list('date', flat=True).distinct()
    types = {paper.type: paper.get_type_display() for paper in papers}
    # Queries
    type_ = request.GET['type']
    author_ = request.GET['author']
    topic_ = request.GET['topic']
    year_ = request.GET['year']
    keyword_ = request.GET['keyword']
    # Type
    if type_:
        papers = papers.filter(type=type_)
    if author_:
        papers = papers.filter(authors=author_)
    if topic_:
        papers = papers.filter(topic=topic_)
    if year_:
        papers = papers.filter(date__year=year_)
    if keyword_:
        papers = papers.filter(abstract__icontains=keyword_) | papers.filter(title__icontains=keyword_) 
    context = {
        'papers': papers,
        'authors': authors,
        'topics': topics,
        'years': [date.year for date in dates],
        'types' : types,
    }
    return render(request, 'papers/papers.html', context)

def paper(request, paper_id):
    paper = get_object_or_404(Paper, pk = paper_id)
    context = {
        'paper': paper
    }
    return render(request, 'papers/paper.html', context)
