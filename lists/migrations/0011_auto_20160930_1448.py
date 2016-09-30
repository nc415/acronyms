# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0010_auto_20160930_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='acronyms',
            name='name_only',
            field=models.CharField(default=datetime.datetime(2016, 9, 30, 12, 48, 30, 85000, tzinfo=utc), max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='emailhistory',
            name='last_emailed',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 30, 14, 48, 23, 829000)),
        ),
    ]
