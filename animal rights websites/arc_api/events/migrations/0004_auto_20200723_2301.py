# Generated by Django 3.0.8 on 2020-07-24 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20200723_2300'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['start_datetime']},
        ),
    ]
