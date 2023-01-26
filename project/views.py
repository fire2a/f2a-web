from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.
def index(request):
    projects = Project.objects.order_by('-name')
    context = {
        'projects': projects,
    }
    return render(request, 'projects/projects.html', context)

def project(request, project_id):
    project = get_object_or_404(Project, pk = project_id)
    context = {
        'project': project
    }
    return render(request, 'projects/project.html', context)
