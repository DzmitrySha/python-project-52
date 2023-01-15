from django.urls import path

from groups.views import (GroupsList, CreateGroup,
                          UpdateGroup, DeleteGroup, GroupDetailView)

urlpatterns = [
    path('', GroupsList.as_view(), name="groups"),
    path('create/', CreateGroup.as_view(), name="group_create"),
    path('<int:pk>/update/', UpdateGroup.as_view(), name="group_update"),
    path('<int:pk>/delete/', DeleteGroup.as_view(), name="group_delete"),
    path('<int:pk>/', GroupDetailView.as_view(), name="group"),
]
