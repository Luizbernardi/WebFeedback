from django.shortcuts import render
from .models import Feedback , Disciplina
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
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
    feedbacks = Feedback.objects.filter(disciplina=disciplinas).order_by('-id')
    return render(request, 'pages/detalhe-disciplina.html', {'disciplinas': disciplinas, 'feedbacks': feedbacks})

@login_required(login_url='login')
def feedback_create_view(request, pk): 
    disciplinas = Disciplina.objects.get(pk=pk)
    if request.method == 'POST':
        nota = request.POST.get('nota')
        comentario = request.POST.get('comentario')

        if not nota or not comentario:
            erro_mensagem = "Por favor, preencha todos os campos."
            return render(request, 'pages/formulario-disciplina.html', {'erro_mensagem': erro_mensagem, 'disciplina_pk': pk})
        
        try:
            nota = int(nota)
            if nota < 1 or nota > 5:
                erro_mensagem = "A nota deve ser um número entre 1 e 5."
                return render(request, 'pages/formulario-disciplina.html', {'erro_mensagem': erro_mensagem, 'disciplina_pk': pk})
        except ValueError:
            erro_mensagem = "A nota deve ser um número válido."
            return render(request, 'pages/formulario-disciplina.html', {'erro_mensagem': erro_mensagem, 'disciplina_pk': pk})
            

        feedback = Feedback(disciplina=disciplinas, nota=nota, comentario=comentario)
        feedback.save()
        return redirect('detalhe_disciplina', pk=pk)
    else:
        return render(request, 'pages/formulario-disciplina.html', {'disciplina_pk': pk})
    
@login_required(login_url='login')
def feedback_edit_view(request, pk):
    
    feedback = Feedback.objects.get(pk=pk)
    disciplina_pk = feedback.disciplina_id

    if request.method == 'POST':
        nota = request.POST.get('nota')
        comentario = request.POST.get('comentario')

        if not nota or not comentario:
            erro_mensagem = "Por favor, preencha todos os campos."
            return render(request, 'pages/editar-feedback-disciplina.html', {'erro_mensagem': erro_mensagem, 'feedback': feedback, 'disciplina_pk': disciplina_pk})

        try:
            nota = int(nota)
            if nota < 1 or nota > 5:
                erro_mensagem = "A nota deve ser um número entre 1 e 5."
                return render(request, 'pages/editar-feedback-disciplina.html', {'erro_mensagem': erro_mensagem, 'feedback': feedback, 'disciplina_pk': disciplina_pk})
        except ValueError:
            erro_mensagem = "A nota deve ser um número válido."
            return render(request, 'pages/editar-feedback-disciplina.html', {'erro_mensagem': erro_mensagem, 'feedback': feedback, 'disciplina_pk': disciplina_pk})

        feedback.nota = nota
        feedback.comentario = comentario
        feedback.save()
        return redirect('detalhe_disciplina', pk=disciplina_pk)

    return render(request, 'pages/editar-feedback-disciplina.html', {'feedback': feedback, 'disciplina_pk': disciplina_pk})
