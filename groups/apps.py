from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class GroupsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'groups'
    verbose_name = _('Groups')
