from django.http import JsonResponse


def students(request):
    breakpoint()
    if request.method == "POST":
        return []
    elif request.method == "GET":
        return []


def get_top_three_students(request):
    return []


def get_top_ten_students(request):
    response = [
      { "idx": 1, "name": "Roberto", "final_score": 10 },
      { "idx": 2, "name": "Fredo", "final_score": 9.9 },
      { "idx": 3, "name": "Roberta", "final_score": 9.8 },
      { "idx": 4, "name": "Paulo", "final_score": 9.7 },
      { "idx": 5, "name": "Tales", "final_score": 9.6 },
      { "idx": 6, "name": "Ana", "final_score": 9.5 },
      { "idx": 7, "name": "Núbia", "final_score": 9.4 },
      { "idx": 8, "name": "Javanil", "final_score": 9.3 },
      { "idx": 9, "name": "Toelison", "final_score": 9.2 },
      { "idx": 10, "name": "Lara", "final_score": 9.1 },
    ]
    return JsonResponse(response, safe=False)
