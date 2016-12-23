# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-23 14:17
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('asuntos', '0003_auto_20161223_0813'),
    ]

    operations = [
        migrations.AddField(
            model_name='asunto',
            name='folio',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
