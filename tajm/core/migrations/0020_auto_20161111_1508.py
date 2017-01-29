# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-11 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20161111_1352'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deadline',
            options={'ordering': ['-ends_at', '-starts_at'], 'verbose_name_plural': 'deadlines'},
        ),
        migrations.RemoveField(
            model_name='deadline',
            name='project',
        ),
        migrations.AddField(
            model_name='deadline',
            name='projects',
            field=models.ManyToManyField(to='tajm.core.Project'),
        ),
    ]
