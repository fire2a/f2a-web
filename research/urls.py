from django.urls import path
from .import views

urlpatterns = [
    path('<int:research_id>', views.research, name = 'research'),
]