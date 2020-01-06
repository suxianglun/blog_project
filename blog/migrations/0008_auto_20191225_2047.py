# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-12-25 12:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20191209_2310'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': '导航栏菜单',
                'verbose_name_plural': '导航栏菜单',
            },
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': '教程', 'verbose_name_plural': '教程'},
        ),
        migrations.AddField(
            model_name='category',
            name='nav_menu',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='blog.NavMenu'),
        ),
    ]
