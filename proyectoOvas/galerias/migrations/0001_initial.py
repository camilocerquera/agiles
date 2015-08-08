# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('url', models.CharField(max_length=2048)),
                ('date', models.DateTimeField()),
                ('user', models.CharField(max_length=16)),
            ],
        ),
    ]
