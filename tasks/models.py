from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Tasks(models.Model):
    name = models.CharField(max_length=120, verbose_name=_('Name'), blank=False)
    description = models.TextField(verbose_name=_('Description'), blank=True)
    created_date = models.DateTimeField(verbose_name=_("Created date"),
                                        default=timezone.now)
    executor = models.ForeignKey(
        to=User, on_delete=models.PROTECT, blank=True, default=None,
    )
    author = models.ForeignKey(
        to=User, on_delete=models.PROTECT, blank=False, default=None,
        related_name='authors',
    )
    status = models.ForeignKey(
        to='statuses.TaskStatus', on_delete=models.PROTECT, blank=True,
        default=None, related_name='statuses',
    )

    def __str__(self):
        return self.name
