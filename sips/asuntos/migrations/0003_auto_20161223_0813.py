# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-23 14:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('asuntos', '0002_asunto'),
    ]

    operations = [
        migrations.AddField(
            model_name='asunto',
            name='added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='asunto',
            name='competencia_ps',
            field=models.BooleanField(default=False, verbose_name='Competencia de la Procuraduria Social'),
        ),
    ]
