from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Home', views.home, name='home'),
    path('Todos', views.todos, name='todos'),
    path('About', views.about, name='about')
]