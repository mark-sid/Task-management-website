from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project_create/', views.project_create, name='project_create'),
    path('project_detail/<project_id>', views.project_detail, name='project_detail'),
    path('project_update/<project_id>', views.project_update, name='project_update'),
    path('project_delete/<project_id>', views.project_delete, name='project_delete'),



]

