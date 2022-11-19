from django.urls import path

from users.views import (UsersList, CreateUser, UpdateUser,
                         DeleteUser, OneUserView)

urlpatterns = [
    path('', UsersList.as_view(), name="users"),
    path('<int:pk>/', OneUserView.as_view(), name="one_user"),
    path('create/', CreateUser.as_view(), name="create"),
    path('<int:pk>/update/', UpdateUser.as_view(), name="update"),
    path('<int:pk>/delete/', DeleteUser.as_view(), name="delete"),
]
