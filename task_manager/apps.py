from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TaskManagerConfig(AppConfig):
    name = 'task_manager'
    verbose_name = _('Task Manager')
