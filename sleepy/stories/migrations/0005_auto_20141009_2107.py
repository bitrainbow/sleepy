# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0004_auto_20141009_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poem',
            name='slug',
            field=models.SlugField(unique=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='shortstory',
            name='slug',
            field=models.SlugField(unique=True, max_length=120),
        ),
    ]
