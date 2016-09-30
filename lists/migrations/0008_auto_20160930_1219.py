# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0007_auto_20160929_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acronyms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='emailhistory',
            name='last_emailed',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 30, 12, 19, 11, 102000)),
        ),
    ]
