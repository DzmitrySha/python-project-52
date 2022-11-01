from django.urls import path

from users.views import (UsersList, CreateUser, UpdateUser,
                         DeleteUser, LoginUser, logout_user)

urlpatterns = [
    path('', UsersList.as_view(), name="users"),
    path('create/', CreateUser.as_view(), name="create"),
    path('<int:pk>/update/', UpdateUser.as_view(), name="update"),
    path('<int:pk>/delete/', DeleteUser.as_view(), name="delete"),
    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', logout_user, name="logout"),
]
