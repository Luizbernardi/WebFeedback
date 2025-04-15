from django.shortcuts import render
from .models import Feedback , Disciplina
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from django.views import View
class HomeView(View):
    def index(request):
        if request.user.is_authenticated:  
            disciplinas = Disciplina.objects.all()  
            return render(request, 'pages/lista-disciplina.html', {'disciplinas': disciplinas})
        else:
            disciplinas = Disciplina.objects.all()  
            return render(request, 'pages/home.html', {'disciplinas': disciplinas})
        
@login_required(login_url='login')
def disciplina_list_view(request):
    disciplinas = Disciplina.objects.all()  
    return render(request, 'pages/lista-disciplina.html', {'disciplinas': disciplinas})

@login_required(login_url='login')
def disciplina_detalhes_view(request, pk):
    disciplinas = Disciplina.objects.get(pk=pk)
    return render(request, 'pages/detalhe-disciplina.html', {'disciplinas': disciplinas})

class FeedbackCreateView(LoginRequiredMixin, CreateView):
    model = Feedback
    template_name = 'pages/formulario-disciplina.html'
    fields = ['nome']
    success_url = reverse_lazy('listagem_disciplina')
    login_url = 'login' 

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return response
    
    