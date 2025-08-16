from django.shortcuts import get_object_or_404, render, redirect
from .forms import ProjectForm
from .models import Project

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects': projects})


def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')  
    else:
        form = ProjectForm()
    return render(request, 'projects/add_project.html', {'form': form})

# def edit_project(request, pk):
#     project = get_object_or_404(Project, pk=pk)
    
#     if request.method == 'POST':
#         form = ProjectForm(request.POST, request.FILES, instance=project)
#         if form.is_valid():
#             form.save()
#             return redirect('projects')  
#         form = ProjectForm(instance=project)
    
#     return render(request, 'projects/edit_project.html', {'form': form, 'project': project})

def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = ProjectForm(instance=project) 

    return render(request, 'projects/edit_project.html', {'form': form, 'project': project})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project.html', {'project': project})