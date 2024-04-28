from django.urls import path
from .views import student_list, student_save

urlpatterns = [
    path('students_list', student_list, name='students_list'),
    path('student_save', student_save, name='student_save'),
    
    
]