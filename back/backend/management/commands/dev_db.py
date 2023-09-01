from django.core.management.base import BaseCommand
from backend.models import Aluno, Atividade, Escola


class Command(BaseCommand):
    help = "Preenche o banco local com informações para usar o aplicativo"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.create_students()
        self.create_schools()
        self.create_activities()

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
        data_school = Escola.objects.create(nome="data")
        technology_school = Escola.objects.create(nome="technology")
        product_school = Escola.objects.create(nome="product")

        names = [
            "Fredo", "Roberta", "Paulo", "Tales", "Ana", "Núbia",
            "Javanil", "Toelison", "Lara", "Roberto"
        ]
        students = Aluno.objects.filter(nome__in=names)

        data_school.alunos.add(students[0])
        data_school.alunos.add(students[1])
        data_school.alunos.add(students[2])
        technology_school.alunos.add(students[2])
        technology_school.alunos.add(students[3])
        technology_school.alunos.add(students[4])
        technology_school.alunos.add(students[5])
        product_school.alunos.add(students[6])
        product_school.alunos.add(students[7])
        product_school.alunos.add(students[8])
        product_school.alunos.add(students[9])

    def create_activities(self):
        fredo = Aluno.objects.get(nome="Fredo")
        roberta = Aluno.objects.get(nome="Roberta")
        paulo = Aluno.objects.get(nome="Paulo")
        tales = Aluno.objects.get(nome="Tales")
        ana = Aluno.objects.get(nome="Ana")
        nubia = Aluno.objects.get(nome="Núbia")
        javanil = Aluno.objects.get(nome="Javanil")
        toelison = Aluno.objects.get(nome="Toelison")
        lara = Aluno.objects.get(nome="Lara")
        roberto = Aluno.objects.get(nome="Roberto")

        data = Escola.objects.get(nome="data")
        technology = Escola.objects.get(nome="technology")
        product = Escola.objects.get(nome="product")

        infos = [
            # Dados
            ## Fredo
            {"student_name": fredo, "activity": "tasks", "grade": 10, "school": data},
            {"student_name": fredo, "activity": "challenges", "grade": 100, "school": data},
            {"student_name": fredo, "activity": "projects", "grade": 80, "school": data},
            ## Roberta
            {"student_name": roberta, "activity": "tasks", "grade": 100, "school": data},
            {"student_name": roberta, "activity": "challenges", "grade": 70, "school": data},
            {"student_name": roberta, "activity": "projects", "grade": 40, "school": data},
            ## Paulo
            {"student_name": paulo, "activity": "tasks", "grade": 30, "school": data},
            {"student_name": paulo, "activity": "challenges", "grade": 30, "school": data},
            {"student_name": paulo, "activity": "projects", "grade": 30, "school": data},
           
            # Tecnologia
            ## Paulo
            {"student_name": paulo, "activity": "tasks", "grade": 70, "school": technology},
            {"student_name": paulo, "activity": "challenges", "grade": 80, "school": technology},
            ## Tales
            {"student_name": tales, "activity": "tasks", "grade": 70, "school": technology},
            {"student_name": tales, "activity": "challenges", "grade": 60, "school": technology},
            {"student_name": tales, "activity": "projects", "grade": 80, "school": technology},
            ## Ana
            {"student_name": ana, "activity": "tasks", "grade": 50, "school": technology},
            {"student_name": ana, "activity": "challenges", "grade": 20, "school": technology},
            {"student_name": ana, "activity": "projects", "grade": 90, "school": technology},
            ## Núbia
            {"student_name": nubia, "activity": "tasks", "grade": 10, "school": technology},
            {"student_name": nubia, "activity": "challenges", "grade": 20, "school": technology},
            {"student_name": nubia, "activity": "projects", "grade": 30, "school": technology},
            
            # Produto
            ## Javanil
            {"student_name": javanil, "activity": "tasks", "grade": 70, "school": product},
            {"student_name": javanil, "activity": "challenges", "grade": 70, "school": product},
            {"student_name": javanil, "activity": "projects", "grade": 70, "school": product},
            ## Toelison
            {"student_name": toelison, "activity": "tasks", "grade": 30, "school": product},
            {"student_name": toelison, "activity": "challenges", "grade": 40, "school": product},
            {"student_name": toelison, "activity": "projects", "grade": 0, "school": product},
            ## Lara
            {"student_name": lara, "activity": "tasks", "grade": 50, "school": product},
            {"student_name": lara, "activity": "challenges", "grade": 80, "school": product},
            {"student_name": lara, "activity": "projects", "grade": 50, "school": product},
            ## Roberto
            {"student_name": roberto, "activity": "tasks", "grade": 50, "school": product},
            {"student_name": roberto, "activity": "challenges", "grade": 50, "school": product},
            {"student_name": roberto, "activity": "projects", "grade": 80, "school": product},
        ]

        activities_to_create = []
        for info in infos:
            activity = Atividade(tipo=info["activity"], nota=info["grade"], aluno=info["student_name"], escola=info["school"])
            activities_to_create.append(activity)

        Atividade.objects.bulk_create(activities_to_create, batch_size=50)
