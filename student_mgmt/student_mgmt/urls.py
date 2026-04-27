from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('student.urls', namespace='student')),
]

# From "student_mgmt/wsgi.py" we come here, where we define the URL patterns for the project.
# We include the URLs from the "student" app in the "student/" path.
# Using this helps to modularize the URL configuration and keeps the project organized.
# The admin interface is also included at the "/admin/" path.
# Each path is mapped to a view or a set of views that will handle the incoming requests and return appropriate responses.
