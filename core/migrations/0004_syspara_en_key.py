# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-02 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_syspara_imgs'),
    ]

    operations = [
        migrations.AddField(
            model_name='syspara',
            name='en_key',
            field=models.CharField(max_length=20, null=True, verbose_name='英文键'),
        ),
    ]
