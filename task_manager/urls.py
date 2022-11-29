from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from task_manager import settings
from task_manager.views import IndexView, LoginUser, LogoutUser

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('admin/', admin.site.urls, name="admin"),
    path('users/', include('users.urls')),
    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', LogoutUser.as_view(), name="logout"),
    path('statuses/', include('statuses.urls')),
    path('labels/', include('labels.urls')),
    path('tasks/', include('tasks.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
