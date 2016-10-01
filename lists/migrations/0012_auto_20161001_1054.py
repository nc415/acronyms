# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0011_auto_20160930_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='society',
            name='notes',
            field=models.TextField(default=b'Notes'),
        ),
        migrations.AlterField(
            model_name='emailhistory',
            name='last_emailed',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 1, 10, 54, 51, 666000)),
        ),
        migrations.AlterField(
            model_name='society',
            name='society_contact_status',
            field=models.CharField(max_length=1, choices=[(b'1', b'Whitelist'), (b'2', b'Blacklist')]),
        ),
    ]
