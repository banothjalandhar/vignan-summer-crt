from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import student_model
from .serializers import student_serializers


@api_view(['GET'])
def get_students(request):

    students = student_model.objects.all()

    serializer = student_serializers(
        students,
        many=True
    )

    return Response(
        serializer.data
    )


@api_view(['POST'])
def add_student(request):

    serializer = student_serializers(
        data=request.data
    )

    if serializer.is_valid():

        serializer.save()

        return Response(
            serializer.data
        )

    return Response(
        serializer.errors
    )


@api_view(['PUT'])
def update_student(request, id):

    student = student_model.objects.get(
        id=id
    )

    serializer = student_serializers(
        student,
        data=request.data
    )

    if serializer.is_valid():

        serializer.save()

        return Response(
            serializer.data
        )

    return Response(
        serializer.errors
    )


@api_view(['DELETE'])
def delete_student(request, id):

    student = student_model.objects.get(
        id=id
    )

    student.delete()

    return Response(
        {
            "message": "Student Deleted"
        }
    )