from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Tasks(models.Model):
    name = models.CharField(max_length=120, verbose_name=_('Name'), blank=False)
    description = models.TextField(verbose_name=_('Description'), blank=True)
# человек на которого задача назначена. Подразумевается, что этот человек её выполняет.
    # executor =
# обязательные поля - автор(устанавливается автоматически при создании задачи) и статус
    # author =
    # status =
