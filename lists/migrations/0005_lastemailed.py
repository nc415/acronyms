# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_auto_20160929_1838'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastEmailed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2016, 9, 29, 18, 44, 37, 998000))),
                ('society', models.ForeignKey(default=0, to='lists.Society')),
            ],
        ),
    ]
