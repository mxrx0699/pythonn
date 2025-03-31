from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.cadastro, name='cadastro'),
]