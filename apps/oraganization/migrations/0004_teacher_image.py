# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-03 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oraganization', '0003_auto_20170402_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(default='', upload_to='teacher/org/%Y/%m', verbose_name='头像'),
        ),
    ]
