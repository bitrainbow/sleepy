from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
from . import models


class PostAdmin(MarkdownModelAdmin):
    list_display = ("title", "date_published")
    prepopulated_fields = {"slug": ("title",)}


class ArticleAdmin():
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(models.Post, PostAdmin)
