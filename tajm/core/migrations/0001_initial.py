# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 23:22
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField(default=15)),
                ('note', models.TextField()),
                ('done_at', models.DateField(default=datetime.date.today)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'progresses',
                'ordering': ['-done_at'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('billable', models.BooleanField(default=True)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'projects',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='progress',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tajm.core.Project'),
        ),
        migrations.AddField(
            model_name='progress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]