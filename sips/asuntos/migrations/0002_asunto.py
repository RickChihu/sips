# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-23 04:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asuntos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asunto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('curp', models.CharField(max_length=100)),
                ('domicilio', models.CharField(max_length=100)),
                ('colonia', models.CharField(max_length=100)),
                ('competencia_ps', models.BooleanField(default=True)),
                ('asunto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asuntos.Tipo')),
            ],
        ),
    ]
