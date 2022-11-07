from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Labels(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(verbose_name=_("Created date"),
                                        default=timezone.now)
