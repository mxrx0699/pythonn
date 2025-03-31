from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.pacotes, name='pacotes'),
]