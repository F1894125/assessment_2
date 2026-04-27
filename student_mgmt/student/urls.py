from django.urls import path
from . import views

app_name = 'student'
# The app_name variable is used to specify the namespace for the URLs in this app.
# This allows us to refer to these URLs unambiguously in other parts of the project.

urlpatterns = [
    path('', views.home , name='home'),
    path('add/', views.add_student, name='add_student'),
    path('display_students/', views.display_students, name='display_students'),
]

# All the paths defined above are mapped to their respective view functions in the "views.py" file of the "student" app.
# These paths specifically handle create and read operations for student records.