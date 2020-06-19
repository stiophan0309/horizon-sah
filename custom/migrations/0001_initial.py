# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-19 19:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Custom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('status', models.CharField(choices=[('new', 'NEW'), ('pending', 'PENDING'), ('in progress', 'IN PROGRESS'), ('complete', 'COMPLETE')], default='new', max_length=20)),
                ('media', models.CharField(choices=[('pastel', 'PASTEL'), ('acrylic', 'ACRYLIC'), ('oil', 'OIL'), ('other', 'OTHER')], default='pastel', max_length=20)),
                ('surface', models.CharField(choices=[('paper', 'PAPER'), ('canvas', 'CANVAS'), ('canvas board', 'CANVAS BOARD'), ('other', 'OTHER')], default='paper', max_length=20)),
                ('size', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to='img')),
                ('details', models.TextField()),
            ],
        ),
    ]
