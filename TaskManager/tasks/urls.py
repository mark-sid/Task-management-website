from django.urls import path
from . import views

urlpatterns = [
    path('task_create/<project_id>', views.task_create, name='task_create'),
    path('task_detail/<task_id>', views.task_detail, name='task_detail'),
    path('task_update/<task_id>', views.task_update, name='task_update'),
    path('task/<task_id>/complete', views.task_completed_field_update, name='task_complete'),
    path('task_delete/<task_id>', views.task_delete, name='task_delete'),
]

