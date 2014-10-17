# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_auto_20141009_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poem',
            name='slug',
            field=models.SlugField(default=b'self.title', max_length=120),
        ),
        migrations.AlterField(
            model_name='shortstory',
            name='slug',
            field=models.SlugField(default=b'self.title', max_length=120),
        ),
    ]
