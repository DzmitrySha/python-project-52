from django.urls import path
from tasks.views import (
    TasksList, OneTaskView, CreateTask, UpdateTask, DeleteTask,
)

urlpatterns = [
    path('', TasksList.as_view(), name="tasks"),
    path('create/', CreateTask.as_view(), name="task_create"),
    path('<int:pk>/update/', UpdateTask.as_view(), name="task_update"),
    path('<int:pk>/delete/', DeleteTask.as_view(), name="task_delete"),
    path('<int:pk>/', OneTaskView.as_view(), name="task_view"),
]
