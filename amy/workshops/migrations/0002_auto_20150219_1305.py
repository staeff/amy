# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='notes',
            field=models.TextField(blank=True, default=''),
            preserve_default=True,
        ),
    ]
