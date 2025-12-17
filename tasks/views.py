from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# LIST all tasks
def task_list(request):
    tasks = Task.objects.all()
    return render(request, "tasks/index.html", {"tasks": tasks})


# ADD new task
def task_add(request):
    if request.method == "POST":
        subject = request.POST.get("subject")
        notes = request.POST.get("notes")

        if subject and notes:
            Task.objects.create(subject=subject, notes=notes)
            return redirect("task_list")

    return render(request, "tasks/add.html")


# EDIT task
def task_edit(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        task.subject = request.POST.get("subject")
        task.notes = request.POST.get("notes")
        task.save()
        return redirect("task_list")

    return render(request, "tasks/edit.html", {"task": task})


# DELETE task
def task_delete(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect("task_list")
