from django.db import models


class BlogQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Post(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    slug = models.SlugField(max_length=120, unique=True)
    publish = models.BooleanField(default=True)
    date_published = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    objects = BlogQuerySet.as_manager()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog Entry'
        verbose_name_plural = 'Blog Entries'
        ordering = ["-date_published"]
