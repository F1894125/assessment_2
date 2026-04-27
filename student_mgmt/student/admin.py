from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'course_name', 'marks']
    list_filter = ['course_name']
    search_fields = ['name', 'email', 'course_name']
    ordering = ['name']
