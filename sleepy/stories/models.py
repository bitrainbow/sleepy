from django.core.urlresolvers import reverse
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.TextField()
    website = models.URLField()

    def __unicode__(self):
        return (self.first_name + ' ' + self.last_name)


class Article(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    author = models.ForeignKey('Author')
    date_published = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=120)

    def __unicode__(self):
        return (self.title + ' - ' + str(self.author))

    class Meta:
        abstract = True


class ShortStory(Article):

    def get_absolute_url(self):
        return reverse("shortstory_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Short Story'
        verbose_name_plural = 'Short Stories'


class Poem(Article):

    def get_absolute_url(self):
        return reverse("poem_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Poem'
        verbose_name_plural = 'Poems'
