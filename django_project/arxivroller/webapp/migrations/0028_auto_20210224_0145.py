# Generated by Django 3.1.5 on 2021-02-24 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0027_auto_20210223_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='arxiv_id',
            field=models.CharField(db_index=True, max_length=50, unique=True),
        ),
    ]
