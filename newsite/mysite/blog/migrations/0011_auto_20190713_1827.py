# Generated by Django 2.1.5 on 2019-07-13 18:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190713_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 13, 18, 27, 48, 454585), verbose_name='published on'),
        ),
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
