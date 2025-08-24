from django.shortcuts import render, redirect, get_object_or_404
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


def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect("students_list")
    else:
        form = StudentForm(instance=student)
        return render(
            request, "students/student_form.html", {"form": form, "edit_mode": True}
        )


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect("students_list")
    else:
        return render(
            request, "students/student_confirm_delete.html", {"student": student}
        )
