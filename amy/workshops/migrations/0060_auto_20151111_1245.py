# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0059_auto_20151109_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='assigned_to',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='eventrequest',
            name='assigned_to',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE),
        ),
    ]
