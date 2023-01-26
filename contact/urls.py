from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='contact_us'),
    path('send_message', views.send, name='send_message'),
]