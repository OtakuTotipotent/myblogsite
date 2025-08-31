from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import StudentForm
from .models import Student


def students_list(request):
    query = request.GET.get("q")
    students = Student.objects.all().order_by("-created_at")
    if query:
        students = students.filter(name__icontains=query) | students.filter(
            email__icontains=query
        )
    return render(
        request, "students/students_list.html", {"students": students, "query": query}
    )


@login_required(login_url="login")
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():
            student = form.save(commit=False)
            student.owner = request.user
            form.save()
            return redirect("students_list")

    else:
        form = StudentForm()

    return render(request, "students/student_form.html", {"form": form})


@login_required(login_url="login")
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk, owner=request.user)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect("students_list")
        else:
            return render(
                request, "students/student_form.html", {"form": form, "edit_mode": True}
            )
    else:
        form = StudentForm(instance=student)
        return render(
            request, "students/student_form.html", {"form": form, "edit_mode": True}
        )


@login_required(login_url="login")
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk, owner=request.user)
    if request.method == "POST":
        student.delete()
        return redirect("students_list")
    else:
        return render(
            request, "students/student_confirm_delete.html", {"student": student}
        )
