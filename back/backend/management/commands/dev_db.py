from django.core.management.base import BaseCommand
from backend.models import Aluno, Atividade, Escola


class Command(BaseCommand):
    help = "Preenche o banco local com informações para usar o aplicativo"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.create_students()
        self.create_schools()

    def create_students(self):
        names = [
            "Roberto", "Fredo", "Roberta", "Paulo", "Tales", "Ana", "Núbia",
            "Javanil", "Toelison", "Lara",
        ]
        students_to_create = []
        for name in names:
            if Aluno.objects.filter(nome=name).exists():
                continue
            student = Aluno(nome=name)
            students_to_create.append(student)

        Aluno.objects.bulk_create(students_to_create, batch_size=50)
    
    def create_schools(self):
        breakpoint()
        schools_to_create = [
            Escola(alunos=["Roberto"], nome=Escola.TIPOS_DE_ESCOLA.DADOS),
            Escola(alunos=["Roberto"], nome=Escola.TIPOS_DE_ESCOLA.TECNOLOGIA),
            Escola(alunos=["Roberto"], nome=Escola.TIPOS_DE_ESCOLA.PRODUTO),
        ]
        Escola.objects.bulk_create(schools_to_create, batch_size=50)

        names = [
            "Fredo", "Roberta", "Paulo", "Tales", "Ana", "Núbia",
            "Javanil", "Toelison", "Lara",
        ]
        students = Aluno.objects.filter(nome__in=names)

        data_school = Escola.objects.get(nome=Escola.TIPOS_DE_ESCOLA.DADOS)
        technology_school = Escola.objects.get(nome=Escola.TIPOS_DE_ESCOLA.TECNOLOGIA)
        product_school = Escola.objects.get(nome=Escola.TIPOS_DE_ESCOLA.PRODUTO)

        data_school.alunos.add(students[0])
        data_school.alunos.add(students[1])
        data_school.alunos.add(students[2])
        technology_school.alunos.add(students[3])
        technology_school.alunos.add(students[4])
        technology_school.alunos.add(students[5])
        product_school.alunos.add(students[6])
        product_school.alunos.add(students[7])
        product_school.alunos.add(students[8])
