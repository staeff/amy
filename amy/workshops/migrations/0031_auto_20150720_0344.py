# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0030_auto_20150720_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='admin_fee',
            field=models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], null=True, decimal_places=2, blank=True, max_digits=6),
        ),
    ]
