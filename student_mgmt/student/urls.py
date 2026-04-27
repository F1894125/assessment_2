from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('', views.home , name='home'),
    path('add/', views.add_student, name='add_student'),
    path('display_students/', views.display_students, name='display_students'),
]