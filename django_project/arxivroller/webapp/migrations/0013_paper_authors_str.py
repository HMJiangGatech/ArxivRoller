# Generated by Django 3.1.5 on 2021-02-20 06:54

import django.contrib.postgres.fields
from django.db import migrations, models

def combine_author_names(apps, schema_editor):
    Paper = apps.get_model('webapp', 'Paper')
    for p in Paper.objects.all():
        p.authors_str = [i['name'] for i in p.authors]
        p.save()

class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_remove_paper_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='authors_str',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=40), null=True, size=None),
        ),
        migrations.RunPython(combine_author_names),
    ]