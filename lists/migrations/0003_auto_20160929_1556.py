# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_auto_20160929_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='Society',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('society_name', models.CharField(unique=True, max_length=256)),
                ('society_acronym', models.CharField(max_length=100)),
                ('society_email', models.EmailField(max_length=254)),
                ('society_status', models.CharField(max_length=1, choices=[(b'P', b'PASSED'), (b'U', b'UNKNOWN'), (b'F', b'FAILED')])),
                ('society_contact_status', models.CharField(max_length=1, choices=[(b'1', b'Positive Response'), (b'2', b'Blacklist')])),
                ('society_slug', models.SlugField(unique=True, blank=True)),
            ],
        ),
        migrations.RenameField(
            model_name='university',
            old_name='acronym',
            new_name='university_acronym',
        ),
        migrations.RenameField(
            model_name='university',
            old_name='name',
            new_name='university_name',
        ),
        migrations.AddField(
            model_name='society',
            name='university',
            field=models.ForeignKey(default=0, to='lists.University'),
        ),
    ]
