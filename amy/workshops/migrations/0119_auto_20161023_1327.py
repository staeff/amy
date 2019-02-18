# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-23 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0118_auto_20160922_0009'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='user_notes',
            field=models.TextField(blank=True, default='', verbose_name='Notes provided by the user in update profile form.'),
        ),
        migrations.AlterField(
            model_name='person',
            name='notes',
            field=models.TextField(blank=True, default='', verbose_name='Admin notes'),
        ),
    ]