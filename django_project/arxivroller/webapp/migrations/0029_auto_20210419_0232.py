# Generated by Django 3.2 on 2021-04-19 06:32

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0028_auto_20210224_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='arxiv_id',
            field=models.CharField(db_index=True, max_length=100, unique=True),
        ),
        migrations.CreateModel(
            name='S2Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s2_id', models.CharField(db_index=True, max_length=100, unique=True)),
                ('arxiv_id', models.CharField(db_index=True, max_length=100, unique=True)),
                ('citation_velocity', models.IntegerField()),
                ('corpus_id', models.IntegerField()),
                ('doi', models.CharField(max_length=100)),
                ('fields_of_study', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=70), size=None)),
                ('influential_citation_count', models.IntegerField()),
                ('is_open_access', models.BooleanField()),
                ('is_publisher_licensed', models.BooleanField()),
                ('topics', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=70), size=None)),
                ('url', models.URLField()),
                ('venue', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('updated', models.DateTimeField()),
                ('citations', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
                ('references', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
                ('paper', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='webapp.paper')),
            ],
        ),
    ]
