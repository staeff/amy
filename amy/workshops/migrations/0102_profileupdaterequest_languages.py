# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0101_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileupdaterequest',
            name='languages',
            field=models.ManyToManyField(blank=True, to='workshops.Language', verbose_name='Languages you can teach in'),
        ),
    ]
