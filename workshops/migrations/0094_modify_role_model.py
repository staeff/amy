# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-22 11:57
from __future__ import unicode_literals

from django.db import migrations, models


def update_roles(apps, schema_editor):
    Role = apps.get_model('workshops', 'Role')

    migrations = [
        ('organizer', 'Workshop organizer'),
        ('learner', 'Learner'),
        ('host', 'Workshop host'),
        ('instructor', 'Instructor'),
        ('helper', 'Helper'),
    ]

    for name, verbose_name in migrations:
        try:
            role = Role.objects.get(name=name)
        except Role.DoesNotExist:
            pass
        else:
            if not role.verbose_name:
                role.verbose_name = verbose_name
            role.save()

    try:
        Role.objects.get(name='contributor')
    except Role.DoesNotExist:
        Role.objects.create(name='contributor',
                            verbose_name='Contributed to lesson materials')


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0093_remove_debriefed_and_tutor_roles'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='verbose_name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.RunPython(update_roles, reverse_code=migrations.RunPython.noop),
    ]
