# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2025-02-14 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailCampaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('html_content', models.TextField()),
                ('send_date', models.DateTimeField(blank=True, null=True)),
                ('subscribers', models.CharField(max_length=255)),
                ('is_sent', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('birthday', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
