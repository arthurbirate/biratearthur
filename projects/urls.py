from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('add/', views.add_project, name='add_project'), 
    path('edit/<int:pk>/', views.edit_project, name='edit_project'),
    # path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path("projects/1/", views.project1_detail, name="project1_detail"),
    path("projects/2/", views.project2_detail, name="project2_detail"),
    path("projects/3/", views.project3_detail, name="project3_detail"),
    path("projects/4/", views.project4_detail, name="project4_detail"),
    path("projects/5/", views.project5_detail, name="project5_detail"),
   
]