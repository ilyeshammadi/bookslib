# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('link_to_pdf', models.URLField()),
                ('thumbnail', models.ImageField(upload_to='books-thumbnail/')),
            ],
        ),
    ]
