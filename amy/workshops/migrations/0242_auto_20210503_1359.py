# Generated by Django 2.2.18 on 2021-05-03 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0241_add_ask_to_repeat_to_training_progress_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingrequest',
            name='state',
            field=models.CharField(choices=[('p', 'Pending'), ('d', 'Discarded'), ('a', 'Accepted'), ('w', 'Withdrawn')], default='p', max_length=1),
        ),
    ]
