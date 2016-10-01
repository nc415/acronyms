# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0013_auto_20161001_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('site_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='emailhistory',
            name='last_emailed',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 1, 11, 28, 4, 493000)),
        ),
        migrations.AlterField(
            model_name='university',
            name='site',
            field=models.ForeignKey(default=0, to='lists.Site'),
        ),
        migrations.AddField(
            model_name='society',
            name='site',
            field=models.ForeignKey(default=0, to='lists.Site'),
        ),
    ]
