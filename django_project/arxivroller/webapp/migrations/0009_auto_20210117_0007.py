# Generated by Django 3.1.5 on 2021-01-17 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_auto_20210117_0006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userpaper',
            old_name='read_state',
            new_name='read_status',
        ),
    ]