# Generated by Django 2.1.5 on 2019-07-14 06:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20190713_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='thumb',
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 14, 6, 35, 17, 122196), verbose_name='published on'),
        ),
    ]