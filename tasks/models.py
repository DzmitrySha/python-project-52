from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
User = get_user_model()


class Tasks(models.Model):
    name = models.CharField(max_length=120, verbose_name=_('Name'), blank=False)
    description = models.TextField(verbose_name=_('Description'), blank=True)
    created_date = models.DateTimeField(verbose_name=_("Created date"),
                                        default=timezone.now)
    executor = models.ForeignKey(
        to=User, on_delete=models.CASCADE, blank=True, null=True, default='',
        related_name='executors', verbose_name=_('Executor'),
    )
    author = models.ForeignKey(
        to=User, on_delete=models.PROTECT, blank=False,
        related_name='authors', verbose_name=_('Author'),
    )
    status = models.ForeignKey(
        to='statuses.TaskStatus', on_delete=models.PROTECT, blank=False,
        related_name='statuses', verbose_name=_('Status'),
    )
    labels = models.ManyToManyField(
        'labels.Label', through='Relations',
        through_fields=('task', 'label'), blank=True,
        related_name='labels', verbose_name=_('Labels'),
    )

    def __str__(self):
        return self.name


class Relations(models.Model):
    task = models.ForeignKey(to='tasks.Tasks', on_delete=models.CASCADE)
    label = models.ForeignKey(to='labels.Label', on_delete=models.PROTECT)
