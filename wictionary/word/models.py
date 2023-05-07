from common.models import TimestampModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class Word(TimestampModel):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name=_("見出し語"))
    meaning = models.CharField(max_length=200, null=False, blank=False, verbose_name=_("意味"))
    phonetic_spelling = models.CharField(max_length=200, null=True, blank=True, verbose_name=_("発音記号"))
    example_sentence = models.TextField(verbose_name=_("例文"))

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["name"]  # 見出し語の昇順
        verbose_name = _("単語")
        verbose_name_plural = verbose_name
