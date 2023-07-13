from modeltranslation.translator import register, TranslationOptions

from . import models


@register(models.News)
class NewsTranslationOption(TranslationOptions):
    fields = ('title', 'body',)


@register(models.Category)
class CategoryTranslationOption(TranslationOptions):
    fields = ('title',)
