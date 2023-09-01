from django.db import models
from django.core.exceptions import ValidationError

# Modelos em pt-br pois outras áreas podem utilizar, então não quero confundir outros analistas

class Aluno(models.Model):
    nome = models.CharField(max_length=100)


class Escola(models.Model):
    TIPOS_DE_ESCOLA = (
        ("data", "dados"),
        ("technology", "tecnologia"),
        ("product", "produto"),
    )
    nome = models.CharField(max_length=20, choices=TIPOS_DE_ESCOLA, unique=True)
    alunos = models.ManyToManyField(Aluno, related_name="escolas")


def validate_interval(value):
    if value >= 0.0 or value <= 100.0:
        raise ValidationError(('%(value)s deve estar entre 0.0 e 100.0'), params={'value': value})


class Atividade(models.Model):
    TIPOS_DE_ATIVIDADES = (
        ("tasks", "tarefas"),
        ("challenges", "desafios"),
        ("projects", "projetos"),
    )
    tipo = models.CharField(max_length=20, choices=TIPOS_DE_ATIVIDADES)
    nota = models.DecimalField(decimal_places=2, max_digits=5, validators=[validate_interval])
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name="atividades_do_aluno")
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE, related_name="atividades_da_escola")
