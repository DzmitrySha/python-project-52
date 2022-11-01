from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from task_manager import settings
from task_manager.views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('admin/', admin.site.urls, name="admin"),
    path('users/', include('users.urls')),
    path('statuses/', include('statuses.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
