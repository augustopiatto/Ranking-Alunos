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
            "Javanil", "Toelison", "Lara", "Vitor", "Joana"
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
            "Roberto", "Fredo", "Roberta", "Paulo", "Tales", "Ana", "Núbia",
            "Javanil", "Toelison", "Lara", "Vitor", "Joana"
        ]
        students = Aluno.objects.filter(nome__in=names)

        data_school.alunos.add(students[0])
        data_school.alunos.add(students[1])
        data_school.alunos.add(students[2])
        data_school.alunos.add(students[3])
        data_school.alunos.add(students[4])
        data_school.alunos.add(students[5])
        data_school.alunos.add(students[6])
        data_school.alunos.add(students[7])
        data_school.alunos.add(students[8])
        data_school.alunos.add(students[9])
        data_school.alunos.add(students[10])
        data_school.alunos.add(students[11])
        technology_school.alunos.add(students[0])
        technology_school.alunos.add(students[1])
        technology_school.alunos.add(students[2])
        technology_school.alunos.add(students[3])
        technology_school.alunos.add(students[4])
        technology_school.alunos.add(students[5])
        technology_school.alunos.add(students[6])
        technology_school.alunos.add(students[7])
        technology_school.alunos.add(students[8])
        technology_school.alunos.add(students[9])
        technology_school.alunos.add(students[10])
        technology_school.alunos.add(students[11])
        product_school.alunos.add(students[0])
        product_school.alunos.add(students[1])
        product_school.alunos.add(students[2])
        product_school.alunos.add(students[3])
        product_school.alunos.add(students[4])
        product_school.alunos.add(students[5])
        product_school.alunos.add(students[6])
        product_school.alunos.add(students[7])
        product_school.alunos.add(students[8])
        product_school.alunos.add(students[9])
        product_school.alunos.add(students[10])
        product_school.alunos.add(students[11])

    def create_activities(self):
        roberto = Aluno.objects.get(nome="Roberto")
        fredo = Aluno.objects.get(nome="Fredo")
        roberta = Aluno.objects.get(nome="Roberta")
        paulo = Aluno.objects.get(nome="Paulo")
        tales = Aluno.objects.get(nome="Tales")
        ana = Aluno.objects.get(nome="Ana")
        nubia = Aluno.objects.get(nome="Núbia")
        javanil = Aluno.objects.get(nome="Javanil")
        toelison = Aluno.objects.get(nome="Toelison")
        lara = Aluno.objects.get(nome="Lara")
        vitor = Aluno.objects.get(nome="Vitor")
        joana = Aluno.objects.get(nome="Joana")

        data = Escola.objects.get(nome="data")
        technology = Escola.objects.get(nome="technology")
        product = Escola.objects.get(nome="product")

        infos = [
            # Dados
            ## Roberto
            {"student_name": roberto, "activity": "tasks", "grade": 10, "school": data},
            {"student_name": roberto, "activity": "challenges", "grade": 10, "school": data},
            {"student_name": roberto, "activity": "projects", "grade": 10, "school": data},
            ## Fredo
            {"student_name": fredo, "activity": "tasks", "grade": 20, "school": data},
            {"student_name": fredo, "activity": "challenges", "grade": 20, "school": data},
            {"student_name": fredo, "activity": "projects", "grade": 20, "school": data},
            ## Roberta
            {"student_name": roberta, "activity": "tasks", "grade": 30, "school": data},
            {"student_name": roberta, "activity": "challenges", "grade": 30, "school": data},
            {"student_name": roberta, "activity": "projects", "grade": 30, "school": data},
            ## Paulo
            {"student_name": paulo, "activity": "tasks", "grade": 40, "school": data},
            {"student_name": paulo, "activity": "challenges", "grade": 40, "school": data},
            {"student_name": paulo, "activity": "projects", "grade": 40, "school": data},
            ## Tales
            {"student_name": tales, "activity": "tasks", "grade": 50, "school": data},
            {"student_name": tales, "activity": "challenges", "grade": 50, "school": data},
            {"student_name": tales, "activity": "projects", "grade": 50, "school": data},
            ## Ana
            {"student_name": ana, "activity": "tasks", "grade": 60, "school": data},
            {"student_name": ana, "activity": "challenges", "grade": 60, "school": data},
            {"student_name": ana, "activity": "projects", "grade": 60, "school": data},
            ## Núbia
            {"student_name": nubia, "activity": "tasks", "grade": 70, "school": data},
            {"student_name": nubia, "activity": "challenges", "grade": 70, "school": data},
            {"student_name": nubia, "activity": "projects", "grade": 70, "school": data},
            ## Javanil
            {"student_name": javanil, "activity": "tasks", "grade": 80, "school": data},
            {"student_name": javanil, "activity": "challenges", "grade": 80, "school": data},
            {"student_name": javanil, "activity": "projects", "grade": 80, "school": data},
            ## Toelison
            {"student_name": toelison, "activity": "tasks", "grade": 90, "school": data},
            {"student_name": toelison, "activity": "challenges", "grade": 90, "school": data},
            {"student_name": toelison, "activity": "projects", "grade": 90, "school": data},
            ## Lara
            {"student_name": lara, "activity": "tasks", "grade": 100, "school": data},
            {"student_name": lara, "activity": "challenges", "grade": 100, "school": data},
            {"student_name": lara, "activity": "projects", "grade": 100, "school": data},
            ## Vitor
            {"student_name": vitor, "activity": "tasks", "grade": 60, "school": data},
            {"student_name": vitor, "activity": "challenges", "grade": 70, "school": data},
            {"student_name": vitor, "activity": "projects", "grade": 80, "school": data},
            ## Joana
            {"student_name": joana, "activity": "tasks", "grade": 65, "school": data},
            {"student_name": joana, "activity": "challenges", "grade": 75, "school": data},
            {"student_name": joana, "activity": "projects", "grade": 85, "school": data},
            
            # Tecnologia
            ## Roberto
            {"student_name": roberto, "activity": "tasks", "grade": 100, "school": technology},
            {"student_name": roberto, "activity": "challenges", "grade": 100, "school": technology},
            {"student_name": roberto, "activity": "projects", "grade": 100, "school": technology},
            ## Fredo
            {"student_name": fredo, "activity": "tasks", "grade": 90, "school": technology},
            {"student_name": fredo, "activity": "challenges", "grade": 90, "school": technology},
            {"student_name": fredo, "activity": "projects", "grade": 90, "school": technology},
            ## Roberta
            {"student_name": roberta, "activity": "tasks", "grade": 80, "school": technology},
            {"student_name": roberta, "activity": "challenges", "grade": 80, "school": technology},
            {"student_name": roberta, "activity": "projects", "grade": 80, "school": technology},
            ## Paulo
            {"student_name": paulo, "activity": "tasks", "grade": 70, "school": technology},
            {"student_name": paulo, "activity": "challenges", "grade": 70, "school": technology},
            {"student_name": paulo, "activity": "projects", "grade": 70, "school": technology},
            ## Tales
            {"student_name": tales, "activity": "tasks", "grade": 60, "school": technology},
            {"student_name": tales, "activity": "challenges", "grade": 60, "school": technology},
            {"student_name": tales, "activity": "projects", "grade": 60, "school": technology},
            ## Ana
            {"student_name": ana, "activity": "tasks", "grade": 50, "school": technology},
            {"student_name": ana, "activity": "challenges", "grade": 50, "school": technology},
            {"student_name": ana, "activity": "projects", "grade": 50, "school": technology},
            ## Núbia
            {"student_name": nubia, "activity": "tasks", "grade": 40, "school": technology},
            {"student_name": nubia, "activity": "challenges", "grade": 40, "school": technology},
            {"student_name": nubia, "activity": "projects", "grade": 40, "school": technology},
            ## Javanil
            {"student_name": javanil, "activity": "tasks", "grade": 30, "school": technology},
            {"student_name": javanil, "activity": "challenges", "grade": 30, "school": technology},
            {"student_name": javanil, "activity": "projects", "grade": 30, "school": technology},
            ## Toelison
            {"student_name": toelison, "activity": "tasks", "grade": 20, "school": technology},
            {"student_name": toelison, "activity": "challenges", "grade": 20, "school": technology},
            {"student_name": toelison, "activity": "projects", "grade": 20, "school": technology},
            ## Lara
            {"student_name": lara, "activity": "tasks", "grade": 10, "school": technology},
            {"student_name": lara, "activity": "challenges", "grade": 10, "school": technology},
            {"student_name": lara, "activity": "projects", "grade": 10, "school": technology},
            ## Vitor
            {"student_name": vitor, "activity": "tasks", "grade": 55, "school": technology},
            {"student_name": vitor, "activity": "challenges", "grade": 75, "school": technology},
            {"student_name": vitor, "activity": "projects", "grade": 35, "school": technology},
            ## Joana
            {"student_name": joana, "activity": "tasks", "grade": 20, "school": technology},
            {"student_name": joana, "activity": "challenges", "grade": 50, "school": technology},
            {"student_name": joana, "activity": "projects", "grade": 60, "school": technology},
            
            # Produto
            ## Roberto
            {"student_name": roberto, "activity": "tasks", "grade": 50, "school": product},
            {"student_name": roberto, "activity": "challenges", "grade": 50, "school": product},
            {"student_name": roberto, "activity": "projects", "grade": 50, "school": product},
            ## Fredo
            {"student_name": fredo, "activity": "tasks", "grade": 40, "school": product},
            {"student_name": fredo, "activity": "challenges", "grade": 40, "school": product},
            {"student_name": fredo, "activity": "projects", "grade": 40, "school": product},
            ## Roberta
            {"student_name": roberta, "activity": "tasks", "grade": 30, "school": product},
            {"student_name": roberta, "activity": "challenges", "grade": 30, "school": product},
            {"student_name": roberta, "activity": "projects", "grade": 30, "school": product},
            ## Paulo
            {"student_name": paulo, "activity": "tasks", "grade": 20, "school": product},
            {"student_name": paulo, "activity": "challenges", "grade": 20, "school": product},
            {"student_name": paulo, "activity": "projects", "grade": 20, "school": product},
            ## Tales
            {"student_name": tales, "activity": "tasks", "grade": 10, "school": product},
            {"student_name": tales, "activity": "challenges", "grade": 10, "school": product},
            {"student_name": tales, "activity": "projects", "grade": 10, "school": product},
            ## Ana
            {"student_name": ana, "activity": "tasks", "grade": 100, "school": product},
            {"student_name": ana, "activity": "challenges", "grade": 100, "school": product},
            {"student_name": ana, "activity": "projects", "grade": 100, "school": product},
            ## Núbia
            {"student_name": nubia, "activity": "tasks", "grade": 90, "school": product},
            {"student_name": nubia, "activity": "challenges", "grade": 90, "school": product},
            {"student_name": nubia, "activity": "projects", "grade": 90, "school": product},
            ## Javanil
            {"student_name": javanil, "activity": "tasks", "grade": 80, "school": product},
            {"student_name": javanil, "activity": "challenges", "grade": 80, "school": product},
            {"student_name": javanil, "activity": "projects", "grade": 80, "school": product},
            ## Toelison
            {"student_name": toelison, "activity": "tasks", "grade": 70, "school": product},
            {"student_name": toelison, "activity": "challenges", "grade": 70, "school": product},
            {"student_name": toelison, "activity": "projects", "grade": 70, "school": product},
            ## Lara
            {"student_name": lara, "activity": "tasks", "grade": 60, "school": product},
            {"student_name": lara, "activity": "challenges", "grade": 60, "school": product},
            {"student_name": lara, "activity": "projects", "grade": 60, "school": product},
            ## Vitor
            {"student_name": vitor, "activity": "tasks", "grade": 15, "school": product},
            {"student_name": vitor, "activity": "challenges", "grade": 95, "school": product},
            {"student_name": vitor, "activity": "projects", "grade": 50, "school": product},
            ## Joana
            {"student_name": joana, "activity": "tasks", "grade": 30, "school": product},
            {"student_name": joana, "activity": "challenges", "grade": 20, "school": product},
            {"student_name": joana, "activity": "projects", "grade": 100, "school": product},
        ]

        activities_to_create = []
        for info in infos:
            activity = Atividade(tipo=info["activity"], nota=info["grade"], aluno=info["student_name"], escola=info["school"])
            activities_to_create.append(activity)

        Atividade.objects.bulk_create(activities_to_create, batch_size=50)
