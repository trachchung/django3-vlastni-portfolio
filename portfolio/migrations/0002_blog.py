# Generated by Django 3.0.6 on 2020-06-06 11:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(max_length=150)),
                ('date', models.DateField(verbose_name=datetime.date.today)),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
