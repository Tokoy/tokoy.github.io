# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-05-04 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.ImageField(default='image/default.png', upload_to='image/%Y/%m'),
        ),
    ]
