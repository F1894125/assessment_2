from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    course_name = models.CharField(max_length=100)
    marks = models.IntegerField()

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name