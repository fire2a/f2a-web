from django.urls import path
from .import views

urlpatterns = [
    path('<int:researcher_id>', views.researcher, name = 'researcher'),
]