# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-16 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gasrecall', '0002_auto_20171208_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gashistory',
            name='taco_meter',
        ),
        migrations.AddField(
            model_name='gashistory',
            name='last_tachometer',
            field=models.IntegerField(default=0, verbose_name='Last Tachometer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gashistory',
            name='tachometer',
            field=models.IntegerField(default=0, verbose_name='Tachometer'),
            preserve_default=False,
        ),
    ]
