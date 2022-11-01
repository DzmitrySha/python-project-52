from django.urls import path

from tasks.views import (TasksList,
                         # CreateTask, UpdateTask,
                         # DeleteTask, ViewTask
                         )

urlpatterns = [
    path('', TasksList.as_view(), name="tasks"),
    # path('create/', CreateTask.as_view(), name="task_create"),
    # path('<int:pk>/update/', UpdateTask.as_view(), name="task_update"),
    # path('<int:pk>/delete/', DeleteTask.as_view(), name="task_delete"),
    # path('<int:pk>/', ViewTask.as_view(), name="task_view"),
]
