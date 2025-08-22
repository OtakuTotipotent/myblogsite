from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

# Create your views here.


def students_list(request):
    students = Student.objects.all()
    return render(request, "students/students_list.html", {"students": students})


def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("students_list")

    else:
        form = StudentForm()

    return render(request, "students/student_form.html", {"form": form})
