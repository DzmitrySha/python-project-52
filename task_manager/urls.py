"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from task_manager import settings
from task_manager.views import UsersList, CreateUser, UpdateUser, DeleteUser

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name="home"),

    path('admin/', admin.site.urls, name="admin"),

    path('users/', UsersList.as_view(), name="users"),

    path('users/create/', CreateUser.as_view(), name="create"),

    path('users/<int:pk>/update/',
         UpdateUser.as_view(template_name="update.html"),
         name="update"),

    path('users/<int:pk>/delete/',
         DeleteUser.as_view(template_name="delete.html"),
         name="delete"),

    path('login/', TemplateView.as_view(template_name="login.html"),
         name="login"),

    path('logout/', TemplateView.as_view(template_name="index.html"),
         name="logout"),

    # path('accounts/', include('django.contrib.auth.urls')),
    # path('i18n/', include('django.conf.urls.i18n')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
