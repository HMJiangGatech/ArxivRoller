# Generated by Django 3.1.5 on 2021-02-22 05:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0021_auto_20210222_0007'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userpaper',
            unique_together={('user', 'paper')},
        ),
    ]
