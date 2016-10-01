# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0016_auto_20161001_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('translation_item', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='emailhistory',
            name='last_emailed',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 1, 16, 30, 16, 72000)),
        ),
    ]
