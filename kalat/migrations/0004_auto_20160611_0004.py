# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-10 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kalat', '0003_kalat_kuva'),
    ]

    operations = [
        migrations.AddField(
            model_name='kalat',
            name='public',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='kalat',
            name='kuva',
            field=models.ImageField(default='images/default.jpg', upload_to='images'),
        ),
    ]
