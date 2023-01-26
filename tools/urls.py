from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='tools'),
    path('<int:tool_id>', views.tool, name = 'tool'),
]