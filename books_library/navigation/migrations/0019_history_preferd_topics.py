# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-22 10:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0021_category_image'),
        ('navigation', '0018_auto_20170521_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='preferd_topics',
            field=models.ManyToManyField(to='books.Category'),
        ),
    ]