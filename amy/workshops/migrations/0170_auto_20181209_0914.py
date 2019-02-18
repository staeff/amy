# Generated by Django 2.1.2 on 2018-12-09 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0169_auto_20181205_1738'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workshoprequest',
            name='part_of_conference',
        ),
        migrations.AlterField(
            model_name='workshoprequest',
            name='conference_details',
            field=models.CharField(blank=True, default='', help_text='If yes, please provide conference details (name, description).', max_length=255, verbose_name='Is this workshop part of conference or larger event?'),
        ),
        migrations.AlterField(
            model_name='workshoprequest',
            name='requested_workshop_types',
            field=models.ManyToManyField(help_text='If your learners are new to programming and primarily interested in working with data, Data Carpentry is likely the best choice. If your learners are interested in learning more about programming, including version control and automation, Software Carpentry is likely the best match. If your learners are people working in library and information related roles interested in learning data and software skills, Library Carpentry is the best choice. Please visit the <a href="https://software-carpentry.org/lessons/">Software Carpentry lessons page</a>, <a href="http://www.datacarpentry.org/lessons/">Data Carpentry lessons page</a>, or the <a href="https://librarycarpentry.org/lessons/">Library Carpentry lessons page</a> for more information about any of our lessons. If you’re not sure and would like to discuss with us, please select the "Don\'t know yet" option below.', limit_choices_to={'active': True}, to='workshops.Curriculum', verbose_name='Which Carpentry workshop are you requesting?'),
        ),
    ]