from django.shortcuts import render, get_object_or_404
from .models import Researcher

# Create your views here.

def researcher(request, researcher_id):
    researcher = get_object_or_404(Researcher, pk = researcher_id)
    mail = researcher.mail.split('@')
    context = {
        'researcher': researcher,
        'mail': mail[0],
        'domain': mail[1],
    }
    return render(request, 'researcher/researcher.html', context)
