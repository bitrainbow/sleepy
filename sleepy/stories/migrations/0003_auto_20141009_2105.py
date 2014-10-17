# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_auto_20141003_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='poem',
            name='slug',
            field=models.SlugField(default=b'self.title', unique=True, max_length=120),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shortstory',
            name='slug',
            field=models.SlugField(default=b'self.title', unique=True, max_length=120),
            preserve_default=True,
        ),
    ]
