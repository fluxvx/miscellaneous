# Generated by Django 3.0.8 on 2020-07-16 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20200716_1525'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='phone_number',
            new_name='phone',
        ),
    ]
