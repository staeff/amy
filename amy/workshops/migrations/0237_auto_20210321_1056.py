# Generated by Django 2.2.17 on 2021-03-21 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0236_organization_coordinates'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membership',
            old_name='seats_instructor_training',
            new_name='public_instructor_training_seats',
        ),
        migrations.RenameField(
            model_name='membership',
            old_name='additional_instructor_training_seats',
            new_name='additional_public_instructor_training_seats',
        ),
        migrations.RenameField(
            model_name='membership',
            old_name='instructor_training_seats_rolled_from_previous',
            new_name='public_instructor_training_seats_rolled_from_previous',
        ),
        migrations.RenameField(
            model_name='membership',
            old_name='instructor_training_seats_rolled_over',
            new_name='public_instructor_training_seats_rolled_over',
        ),
        migrations.AlterField(
            model_name='membership',
            name='public_instructor_training_seats',
            field=models.PositiveIntegerField(default=0, help_text='Number of public seats in instructor trainings', verbose_name='Public instructor training seats'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='additional_public_instructor_training_seats',
            field=models.PositiveIntegerField(default=0, help_text='Use this field if you want to grant more public seats than the agreement provides for.', verbose_name='Additional public instructor training seats'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='public_instructor_training_seats_rolled_from_previous',
            field=models.PositiveIntegerField(blank=True, help_text='Public instructor training seats rolled over from previous membership.', null=True),
        ),
        migrations.AlterField(
            model_name='membership',
            name='public_instructor_training_seats_rolled_over',
            field=models.PositiveIntegerField(blank=True, help_text='Public instructor training seats rolled over into next membership.', null=True),
        ),
        migrations.AddField(
            model_name='membership',
            name='additional_inhouse_instructor_training_seats',
            field=models.PositiveIntegerField(default=0, help_text='Use this field if you want to grant more in-house seats than the agreement provides for.', verbose_name='Additional in-house instructor training seats'),
        ),
        migrations.AddField(
            model_name='membership',
            name='inhouse_instructor_training_seats',
            field=models.PositiveIntegerField(default=0, help_text='Number of in-house seats in instructor trainings', verbose_name='In-house instructor training seats'),
        ),
        migrations.AddField(
            model_name='membership',
            name='inhouse_instructor_training_seats_rolled_from_previous',
            field=models.PositiveIntegerField(blank=True, help_text='In-house instructor training seats rolled over from previous membership.', null=True),
        ),
        migrations.AddField(
            model_name='membership',
            name='inhouse_instructor_training_seats_rolled_over',
            field=models.PositiveIntegerField(blank=True, help_text='In-house instructor training seats rolled over into next membership.', null=True),
        ),
        migrations.RemoveField(
            model_name='membership',
            name='self_organized_workshops_per_agreement',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='self_organized_workshops_rolled_from_previous',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='self_organized_workshops_rolled_over',
        ),

        # The following migration is a no-op as a result of
        # https://github.com/carpentries/amy/pull/1949
        # Previously 0228 introduced `public_status` field with default value of `public`,
        # and this migration changed the default value to `private`. This is however
        # incorrect as the existing memberships need to be migrated with default value
        # of `private` first, thus 0228 was amended to have default value as `private`,
        # and this migration became no-op.
        # migrations.AlterField(
        #     model_name='membership',
        #     name='public_status',
        #     field=models.CharField(choices=[('public', 'Public'), ('private', 'Private')], default='private', help_text='Public memberships may be listed on any of The Carpentries websites.', max_length=20, verbose_name='Can this membership be publicized on The carpentries websites?'),
        # ),
    ]
