from django.shortcuts import render, get_object_or_404
from .models import Research

# Create your views here.

def research(request, research_id):
    research = get_object_or_404(Research, pk = research_id)
    context = {
        'research': research
    }
    return render(request, 'researchs/research.html', context)