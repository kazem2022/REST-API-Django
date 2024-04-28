from django.urls import path
from .views import student_list, student_detail, student_save, student_update


urlpatterns = [
    path('students_list/', student_list),
    path('student_details/<pk>', student_detail),
    path('student_save/', student_save),
    path('student_update/<pk>', student_update),
    
]