# Generated by Django 2.1 on 2018-09-02 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0150_auto_20180902_0231'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='seat_membership',
            field=models.ForeignKey(blank=True, default=None, help_text='In order to count this person into number of used membership instructor training seats, a correct membership entry needs to be selected.', null=True, on_delete=django.db.models.deletion.PROTECT, to='workshops.Membership', verbose_name='Associated member site in TTT event'),
        ),
        migrations.AddField(
            model_name='task',
            name='seat_open_training',
            field=models.BooleanField(blank=True, default=False, help_text='Some TTT events allow for open training; check this field to count this person into open applications.', verbose_name='Open training seat'),
        ),
    ]