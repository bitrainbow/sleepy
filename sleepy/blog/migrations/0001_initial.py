# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('body', models.TextField()),
                ('slug', models.SlugField(unique=True, max_length=120)),
                ('publish', models.BooleanField(default=True)),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-date_published'],
                'verbose_name': 'Blog Entry',
                'verbose_name_plural': 'Blog Entries',
            },
            bases=(models.Model,),
        ),
    ]
