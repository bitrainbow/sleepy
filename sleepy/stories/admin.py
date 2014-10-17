from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
from . import models


class ArticleAdmin(MarkdownModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(models.Author)
admin.site.register(models.ShortStory, ArticleAdmin)
admin.site.register(models.Poem)
