# Generated by Django 3.1.5 on 2021-02-23 06:27

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0023_auto_20210222_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpaper',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), default=list, size=None),
        ),
    ]
