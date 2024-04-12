from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Home', views.home, name='home'),
    path('Todos', views.todos, name='todos'),
    path('About', views.about, name='about'),
    path('delete_todo/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('cancelBtn', views.cancelBtn, name='cancelBtn')
]