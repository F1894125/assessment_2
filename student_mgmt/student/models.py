from django.db import models

# Here we define classes that form the 'M' in the MVT architecture of Django.
# They make the bridge between SQL and Python, allowing us to work with databases using Python code instead of SQL queries.
# This bridge is called ORM (Object Relational Mapping).
# We use QuerySet objects to retrieve data from the database and perform operations on it.
# QuerySet are enabled by model managers, which are used to interact with the database and perform queries on the model's data.

# These models can be registered in the admin interface to allow for easy management of the data through a web interface provided by Django.
# The admin interface is built from "student/admin.py" file.
# Before using the admin interface, we need to create a superuser account using the command "python manage.py createsuperuser" in the terminal.
class Student(models.Model):
    """
    Model representing a student.
    
    Attributes:
        name (str): Name of the student.
        email (str): Email address of the student, must be unique.
        course_name (str): Name of the course the student is enrolled in.
        marks (int): Marks obtained by the student in the course.
    
    Methods:
        __str__: Returns a human readable string for the Student object.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    course_name = models.CharField(max_length=100)
    marks = models.IntegerField()

    class Meta:
        """
         Meta class to define model metadata.
        
        Attributes:
            ordering (list): List of fields to order the Student objects by.
        """
        ordering = ['name']
    
    def __str__(self):
        """
        Returns a human readable string for the current Student object.
        
        Returns:
            str: The name of the student.
        """
        return self.name