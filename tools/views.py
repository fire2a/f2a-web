from django.shortcuts import render, get_object_or_404
from .models import Tools

# Create your views here.
def index(request):
    tools = Tools.objects.order_by('-name')
    context = {
        'tools': tools,
    }
    return render(request, 'tools/tools.html', context)

def tool(request, tool_id):
    tool = get_object_or_404(Tools, pk = tool_id)
    context = {
        'tool': tool
    }
    return render(request, 'tools/tool.html', context)