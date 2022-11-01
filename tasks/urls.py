from django.urls import path

from users.views import (UsersList,
                         # CreateTask, UpdateTask,
                         # DeleteTask, ViewTask
                         )

urlpatterns = [
    # path('', TasksList.as_view(), name="tasks"),
    # path('create/', CreateTask.as_view(), name="create"),
    # path('<int:pk>/update/', UpdateTask.as_view(), name="update"),
    # path('<int:pk>/delete/', DeleteTask.as_view(), name="delete"),
    # path('<int:pk>/', ViewTask.as_view(), name="view"),
]
