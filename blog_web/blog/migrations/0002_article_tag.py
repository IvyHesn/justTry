# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.CharField(default=datetime.datetime(2015, 4, 24, 8, 24, 29, 57000, tzinfo=utc), max_length=20, verbose_name='Article_tag'),
            preserve_default=False,
        ),
    ]
