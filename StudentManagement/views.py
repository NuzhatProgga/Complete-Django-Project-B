from django.shortcuts import render
from .models import Student
from .forms import StudentInsertForm
# Create your views here.

def showStudentList(request):
    all_students = Student.objects.all()
    context = {
        'studentList' : all_students
    }
    return render(request, 'StudentManagement/studentslist.html', context)


def insertStudents(request):

    form = StudentInsertForm()
    message = "Insert Student info"

    if request.method == "POST":
        form = StudentInsertForm(request.POST)
        message = "Not Successful"
        if form.is_valid():
            form.save()
            form = StudentInsertForm()
            message = "Successful"

    context = {
        'form' : form,
        'message' : message
    }
    return render(request, 'StudentManagement/insertStudent.html', context)