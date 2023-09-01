def get_students_serializer(obj):
    return {
        "id": obj.id,
        "name": obj.nome
    }
