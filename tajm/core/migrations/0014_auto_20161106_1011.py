# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-06 10:11
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('core', '0013_auto_20160518_0712'),
    ]

    operations = [
        migrations.CreateModel(
            name='TajmUser',
            fields=[
            ],
            options={
                'db_table': 'auth_user',
                'proxy': True,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='absence',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tajm.core.TajmUser'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tajm.core.TajmUser'),
        ),
    ]
