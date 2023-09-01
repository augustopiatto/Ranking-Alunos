def get_students_serializer(obj):
    return {
        "id": obj.id,
        "name": obj.nome
    }


def get_top_students_serializer(index, obj):
    return {
        "idx": index + 1,
        "name": obj["aluno__nome"],
        "final_score": obj["grade_avg"] if obj.get("grade_avg") else None
    }
