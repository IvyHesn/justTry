# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='Article_name')),
                ('content', models.TextField(verbose_name='Article_content')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='pub_date')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='update_time', null=True)),
            ],
        ),
    ]
