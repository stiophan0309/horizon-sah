# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-15 19:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('details', models.TextField()),
                ('media', models.BooleanField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.DeleteModel(
            name='Work',
        ),
        migrations.AddField(
            model_name='feedback',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commissions.Product'),
        ),
    ]
