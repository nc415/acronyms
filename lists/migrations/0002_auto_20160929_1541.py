# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='rag',
            field=models.CharField(max_length=1, choices=[(b'Y', b'Yes'), (b'N', b'No')]),
        ),
    ]
