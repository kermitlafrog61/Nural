from modeltranslation.translator import translator, TranslationOptions

from . import models


class NewsTranslationOption(TranslationOptions):
    fields = ('title', 'body',)


class CategoryTranslationOption(TranslationOptions):
    fields = ('title',)


translator.register(models.News, NewsTranslationOption)
translator.register(models.Category, CategoryTranslationOption)
