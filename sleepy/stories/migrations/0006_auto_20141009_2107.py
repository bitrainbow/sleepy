# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0005_auto_20141009_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poem',
            name='slug',
            field=models.SlugField(max_length=120),
        ),
        migrations.AlterField(
            model_name='shortstory',
            name='slug',
            field=models.SlugField(max_length=120),
        ),
    ]
