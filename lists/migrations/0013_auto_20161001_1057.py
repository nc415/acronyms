# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0012_auto_20161001_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailhistory',
            name='last_emailed',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 1, 10, 57, 37, 197000)),
        ),
        migrations.AlterField(
            model_name='society',
            name='notes',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='society',
            name='society_acronym',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='society',
            name='society_email',
            field=models.EmailField(max_length=254, blank=True),
        ),
    ]
