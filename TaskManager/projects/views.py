from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from tasks.models import Task
from .forms import ProjectCreateForm, ProjectUpdateForm
from .models import Project
from django.views.decorators.http import require_POST

# Create your views here.


def home(request):
    template_name = 'projects/home.html'
    user_authentication = request.user.is_authenticated
    if user_authentication:
        projects = Project.objects.filter(user=request.user)

        return render(request, template_name, {'user_authentication': user_authentication, 'projects': projects})

    return render(request, template_name, {'user_authentication': user_authentication})


@login_required
def project_detail(request, project_id):
    template_name = 'projects/project_detail.html'
    project = get_object_or_404(Project, id=project_id, user=request.user)
    tasks = Task.objects.filter(project=project)
    return render(request, template_name, {'project': project, 'tasks':tasks})


@login_required
def project_create(request):
    template_name = 'projects/project_create.html'
    if request.method == 'POST':
        form = ProjectCreateForm(request.POST, user=request.user)
        if form.is_valid():
            project = form.save()
            return redirect('project_detail', project_id=project.id)
        return render(request, template_name, {'form': form})

    form = ProjectCreateForm()
    return render(request, template_name, {'form': form})


@login_required
def project_update(request, project_id):
    template_name = 'projects/project_update.html'
    project = get_object_or_404(Project, id=project_id, user=request.user)

    if request.method == 'POST':
        form = ProjectUpdateForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', project_id=project.id)

    form = ProjectUpdateForm(instance=project)
    return render(request, template_name, {'form': form, 'project': project})


@login_required
@require_POST
def project_delete(request, project_id):
    project = get_object_or_404(Project, id=project_id, user=request.user)
    project.delete()
    return redirect('home')
