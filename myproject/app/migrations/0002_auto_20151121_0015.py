# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scraped_item',
            name='desc',
        ),
        migrations.AddField(
            model_name='scraped_item',
            name='category',
            field=models.CharField(default=datetime.date(2015, 11, 21), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scraped_item',
            name='location',
            field=models.CharField(default='Dhaka', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scraped_item',
            name='posting_time',
            field=models.CharField(default=datetime.date(2015, 11, 21), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scraped_item',
            name='price',
            field=models.CharField(default='2000', max_length=100),
            preserve_default=False,
        ),
    ]
