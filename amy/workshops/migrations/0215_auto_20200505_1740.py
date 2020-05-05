# Generated by Django 2.2.10 on 2020-05-05 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0214_workshoprequest_online_inperson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshoprequest',
            name='online_inperson',
            field=models.CharField(choices=[('online', 'Online'), ('inperson', 'In-person'), ('unsure', 'Not sure')], default=None, max_length=15, verbose_name='Will this workshop be held online or in-person?'),
        ),
    ]