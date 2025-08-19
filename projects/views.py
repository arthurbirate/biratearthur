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


from django.shortcuts import render, get_object_or_404
from .models import Project

# Project 1 - YOLOv5/YOLOv8
def project1_detail(request):
    project = get_object_or_404(Project, id=1)
    return render(request, "projects/waldo.html", {
        "image1": project.image1,
        "image2": project.image2,
        "project": project, 
    })

# Project 5 - HR Analytics Dashboard
def project2_detail(request):
    project = get_object_or_404(Project, id=5)
    return render(request, "projects/hr.html", {
        "image1": project.image1,
        "image2": project.image2,
        "project": project,
    })

# Project 2 - VisiAge
def project3_detail(request):
    project = get_object_or_404(Project, id=2)
    return render(request, "projects/visiAge.html", {
        "image1": project.image1,
        "image2": project.image2,
        "project": project,
    })

# Project 3 - Olympics Dashboard
def project4_detail(request):
    project = get_object_or_404(Project, id=3)
    return render(request, "projects/olympic.html", {
        "image1": project.image1,
        "image2": project.image2,
        "project": project,
    })

# Project 4 - Superstore Analytics
def project5_detail(request):
    project = get_object_or_404(Project, id=4)
    return render(request, "projects/superstore.html", {
        "image1": project.image1,
        "image2": project.image2,
        "project": project,
    })
