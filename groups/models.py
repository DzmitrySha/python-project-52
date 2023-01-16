from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Group(models.Model):
    name = models.CharField(max_length=120, blank=False, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_('Description'), blank=True)
    created_date = models.DateTimeField(verbose_name=_("Created date"),
                                        default=timezone.now)
    creator = models.ForeignKey(
        to='users.User', on_delete=models.PROTECT, blank=False,
        related_name='creator', verbose_name=_('Creator'),
    )
    participants = models.ManyToManyField(
        to='users.User', through='GroupRelations',
        through_fields=('group', 'participant'), blank=True,
        related_name='participants', verbose_name=_('Participants'),
    )

    def __str__(self):
        return self.name


class GroupRelations(models.Model):
    group = models.ForeignKey(to='groups.Group', on_delete=models.CASCADE)
    participant = models.ForeignKey(to='users.User', on_delete=models.PROTECT)
