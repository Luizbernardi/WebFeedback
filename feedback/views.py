from django.shortcuts import render
from .models import Feedback , Disciplina

# Create your views here.
class HomeView(View):
    def index(request):
        if request.user.is_authenticated:  
            disciplinas = Disciplina.objects.all()  
            return render(request, 'feedback/lista-disciplina.html', {'disciplinas': disciplinas})
        else:
            disciplinas = Disciplina.objects.all()  
            return render(request, 'feedback/home.html', {'disciplinas': disciplinas})