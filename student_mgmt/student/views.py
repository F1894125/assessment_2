from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpRequest
from .models import Student

def home(request: HttpRequest) -> HttpResponse:
    """
    Function-based view that renders the home page of the student management application.
    Takes an HTTP request as argument and returns an HTTP response that renders the 'student/home.html'. 

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    return render(request, 'student/home.html')

def add_student(request: HttpRequest) -> HttpResponse:
    """
    Function-based view that adds a new student to the database.
    Handles both GET and POST requests.
    
    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object that renders the 'student/add_student.html' template.
    """
    students = Student.objects.all() # Queryset to retrieve all Student objects from the database and store them in the variable 'students'.

    if request.method == 'POST': # Checks if the request method is POST, indicating that the form has been submitted.
        if all(request.POST.values()): # Checks if all form fields are filled.
            id = request.POST.get('id') # Retrieves the student_id from the form data.
            if id in students.values_list('id', flat=True): # Checks if a student with the same ID already exists in the database. 
                messages.error(request, f"Student with ID '{id}' already exists.") # Adds an error message to the messages framework if a duplicate ID is found.
                return redirect('student:add_student') # Redirects the user back to the add student page if a duplicate ID is found.

            student = Student(
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                course_name=request.POST.get('course_name'),
                marks=request.POST.get('marks')
            ) # Creates a new Student object with the data retrieved from the form fields.

            student.save() # Saves the new Student object to the database, adding a new record to the Student table.
            messages.success(request, f"Student '{student.name}' added.") # Adds a success message to the messages framework indicating that the student was added successfully.
            return redirect('student:add_student')
        
        else: # If any form field is left empty, an error message is added to the messages, and the user is redirected back to the add student page.
            messages.error(request, "Please fill all the fields.")
            return redirect('student:add_student')
    
    return render(request, 'student/add_student.html')


def display_students(request: HttpRequest) -> HttpResponse:
    """
    Function-based view that shows all the students.
    
    Args:
        request (HttpRequest): The HTTP request object.
    
    Returns:
        HttpResponse: The HTTP response object that renders the 'student/display_students.html' template.
    """
    students = Student.objects.all()
    context = {'students': students} # Creates a context dictionary that contains the queryset of all Student objects, which will be passed to the template for rendering.

    return render(request, 'student/display_students.html', context)