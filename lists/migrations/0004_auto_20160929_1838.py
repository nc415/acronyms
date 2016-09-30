# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_auto_20160929_1556'),
    ]

    operations = [
        migrations.RenameField(
            model_name='society',
            old_name='society_status',
            new_name='society_email_status',
        ),
    ]
