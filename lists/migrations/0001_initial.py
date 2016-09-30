# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('site', models.CharField(max_length=1, choices=[(b'L', b'London'), (b'O', b'Oxford'), (b'C', b'Cambridge')])),
                ('name', models.CharField(unique=True, max_length=128)),
                ('acronym', models.CharField(unique=True, max_length=128)),
                ('rag', models.CharField(max_length=1, choices=[(b'Y', b'Has RAG'), (b'N', b'No RAG')])),
                ('slug', models.SlugField(unique=True, blank=True)),
            ],
        ),
    ]
