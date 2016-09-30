# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0009_auto_20160930_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailhistory',
            name='last_emailed',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 30, 13, 6, 28, 475000)),
        ),
    ]
