from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='offers'),
    path('<offer_id>', views.offer, name = 'offer'),
]