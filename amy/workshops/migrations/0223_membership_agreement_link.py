# Generated by Django 2.2.17 on 2020-11-29 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0222_workshoprequest_workshop_listed'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='agreement_link',
            field=models.URLField(blank=True, default='', help_text='Link to member agreement document or folder in Google Drive', verbose_name='Link to member agreement'),
        ),
    ]
