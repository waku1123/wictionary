from django.db import models
from django.utils.translation import gettext_lazy as _


class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("作成日"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("更新日"))

    class Meta:
        abstract = True
