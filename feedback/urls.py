from django.urls import path
from . import views
from .views import  HomeView

urlpatterns = [
    path('', HomeView.index, name='home'),
    path('disciplinas', views.disciplina_list_view, name='listagem_disciplina'),
    path('disciplinas/<int:pk>/',views.disciplina_detalhes_view, name='detalhe'),
]