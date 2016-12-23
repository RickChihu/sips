# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-23 17:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asuntos', '0008_auto_20161223_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='asunto',
            name='municipio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='asuntos.Municipio'),
            preserve_default=False,
        ),
    ]
