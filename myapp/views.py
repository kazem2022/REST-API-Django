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

@api_view(["POST"])
def student_save(request):
    student = StudentSerializer(data=request.data)
    if student.is_valid():
        student.save()
    return Response(student.data)

@api_view(["POST", "GET"])
def student_update(request, pk):
    instancee = Student.objects.get(id=pk)
    student = StudentSerializer(instance=instancee, data=request.data)
    student_now = StudentSerializer(instancee, many=False)
    if student.is_valid():
        student.save()
    return Response( student_now.data)

@api_view(["DELETE"])
def student_delete(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return Response(f"student:{student} deleted!")


    