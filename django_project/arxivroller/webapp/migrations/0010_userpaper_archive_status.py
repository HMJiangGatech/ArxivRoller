# Generated by Django 3.1.5 on 2021-02-16 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_auto_20210117_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpaper',
            name='archive_status',
            field=models.BooleanField(default=False),
        ),
    ]
