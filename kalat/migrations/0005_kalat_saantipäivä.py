# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-31 19:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('kalat', '0004_auto_20160611_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='kalat',
            name='saantipäivä',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 31, 19, 7, 0, 327075, tzinfo=utc), verbose_name='date published'),
            preserve_default=False,
        ),
    ]
