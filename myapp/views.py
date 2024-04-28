from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer

@api_view(["GET"])
def student_list(request):
    students = Student.objects.all()
    students_serializers = StudentSerializer(students, many=True)
    return Response(students_serializers.data)

@api_view(["GET"])
def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    student_serializer = StudentSerializer(student, many=False)
    return Response(student_serializer.data)