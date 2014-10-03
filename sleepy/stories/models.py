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

    class Meta:
        abstract = True


class ShortStory(Article):
    def __unicode__(self):
        return (self.title + ' - ' + str(self.author))

    class Meta:
        verbose_name = 'Short Story'
        verbose_name_plural = 'Short Stories'


class Poem(Article):
    def __unicode__(self):
        return (self.title + ' - ' + str(self.author))

    class Meta:
        verbose_name = 'Poem'
        verbose_name_plural = 'Poems'
