# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0006_auto_20160929_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailhistory',
            name='last_emailed',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 29, 19, 22, 35, 521000)),
        ),
    ]
