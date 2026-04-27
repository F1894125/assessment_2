from django.apps import AppConfig

# Here we define the configuration for the 'student' app.
# This class is used by Django to set up the app and its components.

class StudentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'student'
