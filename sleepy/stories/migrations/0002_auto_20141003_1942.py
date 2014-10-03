# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='poem',
            options={'verbose_name': 'Poem', 'verbose_name_plural': 'Poems'},
        ),
        migrations.AlterModelOptions(
            name='shortstory',
            options={'verbose_name': 'Short Story', 'verbose_name_plural': 'Short Stories'},
        ),
    ]
