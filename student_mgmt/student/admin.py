from django.contrib import admin
from .models import Student

# Here we register the Student model with the admin site to enable management of student data through the Django admin interface.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'course_name', 'marks']
    list_filter = ['course_name']
    search_fields = ['name', 'email', 'course_name']
    ordering = ['name']
