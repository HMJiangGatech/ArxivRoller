# Generated by Django 3.1.5 on 2021-02-17 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_userpaper_archive_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpaper',
            name='star_status',
            field=models.BooleanField(default=False),
        ),
    ]