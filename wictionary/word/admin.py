from django.contrib import admin

from .models import Word


@admin.register(Word)
class WordAdmin:
    list_display = ("name", "meaning", "phonetic_spelling", "example_sentence")
