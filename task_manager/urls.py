from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from task_manager import settings
from task_manager.views import (UsersList, CreateUser, UpdateUser,
                                DeleteUser, LoginUser, logout_user, IndexView)

urlpatterns = [
    # path('', TemplateView.as_view(template_name="index.html"), name="home"),
    path('', IndexView.as_view(), name="home"),
    path('admin/', admin.site.urls, name="admin"),
    path('users/', UsersList.as_view(), name="users"),
    path('users/create/', CreateUser.as_view(), name="create"),
    path('users/<int:pk>/update/', UpdateUser.as_view(), name="update"),
    path('users/<int:pk>/delete/', DeleteUser.as_view(), name="delete"),
    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', logout_user, name="logout"),

    # path('accounts/', include('django.contrib.auth.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
