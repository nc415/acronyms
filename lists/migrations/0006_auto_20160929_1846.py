# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_lastemailed'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_emailed', models.DateTimeField(default=datetime.datetime(2016, 9, 29, 18, 46, 18, 324000))),
                ('society', models.ForeignKey(default=0, to='lists.Society')),
            ],
        ),
        migrations.RemoveField(
            model_name='lastemailed',
            name='society',
        ),
        migrations.DeleteModel(
            name='LastEmailed',
        ),
    ]
