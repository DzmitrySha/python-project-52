from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from statuses.models import TaskStatus


# Create your models here.
class Tasks(models.Model):
    name = models.CharField(max_length=120, verbose_name=_('Name'), blank=False)
    description = models.TextField(verbose_name=_('Description'), blank=True)

    # Человек, на которого задача назначена.
    # Подразумевается, что этот человек её выполняет.
    # executor = models.OneToOneField(User, on_delete=models.CASCADE)

    # обязательные поля - автор(устанавливается автоматически
    # при создании задачи) и статус
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               default=None, blank=False)
    status = models.ForeignKey(TaskStatus, on_delete=models.CASCADE,
                               default=None, blank=True)
