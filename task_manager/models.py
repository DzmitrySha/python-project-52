from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class TaskStatus(models.Model):
    name = models.CharField(max_length=120, blank=False)
    created_date = models.DateTimeField(_("Created date"), default=timezone.now)
