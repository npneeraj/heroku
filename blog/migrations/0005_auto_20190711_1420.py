# Generated by Django 2.1.5 on 2019-07-11 14:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190711_1154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='published',
        ),
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 11, 14, 20, 42, 262044), verbose_name='date published'),
        ),
    ]
