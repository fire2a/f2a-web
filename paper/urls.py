from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='papers'),
    path('search_papers', views.search, name='search_papers'),
    path('<paper_id>', views.paper, name = 'paper'),
]