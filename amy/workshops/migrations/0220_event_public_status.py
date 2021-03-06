# Generated by Django 2.2.13 on 2020-10-18 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0219_workshoprequest_online_inperson'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='public_status',
            field=models.CharField(choices=[('public', 'Public'), ('private', 'Private')], default='public', blank=True, max_length=10, verbose_name='Is this workshop public?', help_text='Public workshops will show up in public Carpentries feeds.'),
        ),
    ]
