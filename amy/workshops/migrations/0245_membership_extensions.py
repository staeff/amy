# Generated by Django 2.2.18 on 2021-05-17 06:36

import django.contrib.postgres.fields
from django.db import migrations, models


def move_extensions(apps, schema_editor):
    """Move existing `extended` value into the new field `extensions`."""
    Membership = apps.get_model('workshops', 'Membership')
    for membership in Membership.objects.all():
        membership.extensions = (
            [] if membership.extended is None
            else [membership.extended]
        )
        membership.save()


def undo_extensions(apps, schema_editor):
    """Move from `extensions` to single value `extended` field."""
    Membership = apps.get_model('workshops', 'Membership')
    for membership in Membership.objects.all():
        membership.extended = sum(membership.extensions) or None
        membership.save()


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0244_auto_20210509_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='extensions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), default=list, help_text='Number of days the agreement was extended. The field stores multiple extensions. The agreement end date has been moved by a cumulative number of days from this field.', size=None),
        ),
        migrations.RunPython(move_extensions, undo_extensions),
        migrations.RemoveField(
            model_name='membership',
            name='extended',
        ),
    ]
