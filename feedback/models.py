from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Feedback(models.Model):
    nota = models.IntegerField(
        verbose_name="Nota",
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comentario = models.CharField(max_length=200, verbose_name="Comentario")

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome")
    professor = models.CharField(max_length=200, verbose_name="Professor")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descricao")
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE, verbose_name="Feedback")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"
        ordering = ["nome"]
