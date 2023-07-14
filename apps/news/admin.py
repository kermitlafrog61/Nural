from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline

from . import models


@admin.register(models.News)
class NewsAdmin(TranslationAdmin):
    list_display = ('title', 'category')


@admin.register(models.Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('title',)
