from django.shortcuts import render
from .models import Feedback , Disciplina
from django.contrib.auth.decorators import login_required

from django.views import View
class HomeView(View):
    def index(request):
        if request.user.is_authenticated:  
            disciplinas = Disciplina.objects.all()  
            return render(request, 'feedback/pages/lista-disciplina.html', {'disciplinas': disciplinas})
        else:
            disciplinas = Disciplina.objects.all()  
            return render(request, 'feedback/pages/home.html', {'disciplinas': disciplinas})
        
@login_required(login_url='login')
def disciplina_list_view(request):
    disciplinas = Disciplina.objects.all()  
    return render(request, 'feedback/pages/lista-disciplina.html', {'disciplinas': disciplinas})

@login_required(login_url='login')
def disciplina_detalhes_view(request, pk):
    disciplinas = Disciplina.objects.get(pk=pk)
    return render(request, 'feedback/pages/detalhe-disciplina.html', {'disciplinas': disciplinas})