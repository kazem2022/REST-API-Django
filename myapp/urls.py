from django.urls import path
from .views import student_list, student_detail


urlpatterns = [
    path('students_list/', student_list),
    path('student_details/<pk>', student_detail),
    
    
]