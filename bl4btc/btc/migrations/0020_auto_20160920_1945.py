# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 19:45
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('btc', '0019_auto_20160919_1902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sellurls',
            name='id',
        ),
        migrations.AddField(
            model_name='sellurls',
            name='urluuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sellurls',
            name='tags',
            field=models.CharField(default=None, max_length=255),
        ),
    ]