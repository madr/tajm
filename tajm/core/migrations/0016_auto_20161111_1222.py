# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-11 12:22
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models

import tajm.core.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20161106_1016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deadline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=128)),
                ('ends_at', models.DateField(null=True)),
                ('starts_at', models.DateField(null=True)),
                ('amount', models.IntegerField(null=True, validators=[tajm.core.models.validate_duration])),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tajm.core.Project')),
            ],
        ),
        migrations.AlterField(
            model_name='absence',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tajm.core.AbsenceCategory'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tajm.core.Project'),
        ),
    ]