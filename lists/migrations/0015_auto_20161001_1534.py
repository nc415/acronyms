# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0014_auto_20161001_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailhistory',
            name='last_emailed',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 1, 15, 34, 41, 499000)),
        ),
        migrations.AlterField(
            model_name='site',
            name='site_name',
            field=models.CharField(unique=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='society',
            name='society_contact_status',
            field=models.CharField(max_length=1, choices=[(b'1', b'Whitelist'), (b'2', b'Blacklist'), (b'3', b'Neutral')]),
        ),
    ]
