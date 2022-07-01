#!/
from django.urls import path

from . import views
from .api import endpoints

app_name = 'shortener'
urlpatterns = [
    path('', views.index, name='index'),
    path('api/shortener/', endpoints.Index, name='api_setURL'),
    path('<str:name>/', views.rerouter, name='shorturl'),
]