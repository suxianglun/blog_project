# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-31 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190731_1614'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='img',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='post',
            name='img_url',
            field=models.URLField(blank=True, verbose_name='图片外部url'),
        ),
    ]
