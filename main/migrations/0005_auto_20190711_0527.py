# Generated by Django 2.1.5 on 2019-07-11 05:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190317_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 11, 5, 27, 14, 139422), verbose_name='date published'),
        ),
    ]
