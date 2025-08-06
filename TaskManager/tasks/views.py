from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskCreateForm, TaskUpdateForm
from projects.models import Project
from .models import Task
from django.http import JsonResponse
from django.http import HttpResponseForbidden
from django.views.decorators.http import require_POST
import json


# Create your views here.

@login_required
def task_create(request, project_id):
    template_name = 'tasks/task_create.html'
    if request.method == 'POST':
        project = get_object_or_404(Project, id=project_id, user=request.user)
        form = TaskCreateForm(request.POST, project=project)
        if form.is_valid():
            task = form.save()
            return redirect('task_detail', task_id=task.id)
        return render(request, template_name, {'form': form, 'project_id': project_id})

    form = TaskCreateForm()
    return render(request, template_name, {'form': form, 'project_id': project_id})


@login_required
def task_detail(request, task_id):
    template_name = 'tasks/task_detail.html'
    task = get_object_or_404(Task, id=task_id)
    project = task.project
    if project.user != request.user:
        return HttpResponseForbidden("Access denied.")

    return render(request, template_name, {'project_id': project.id, 'task':task})

@login_required
@require_POST
def task_completed_field_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if task.project.user != request.user:
        return HttpResponseForbidden("Access denied.")

    data = json.loads(request.body)

    task.completed = data.get('completed', False)
    task.save()

    return JsonResponse({'success': True})


@login_required
def task_update(request, task_id):
    template_name = 'tasks/task_update.html'
    task = get_object_or_404(Task, id=task_id)

    if task.project.user != request.user:
        return HttpResponseForbidden("Access denied.")

    if request.method == 'POST':
        form = TaskUpdateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', task_id=task.id)

    form = TaskUpdateForm(instance=task)
    return render(request, template_name, {'form': form, 'task': task })



@login_required
@require_POST
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    project = task.project

    if project.user != request.user:
        return HttpResponseForbidden("Access denied.")

    task.delete()
    return redirect('project_detail', project_id=project.id)