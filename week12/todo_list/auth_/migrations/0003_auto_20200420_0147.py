# Generated by Django 3.0.4 on 2020-04-20 01:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auth_', '0002_auto_20200420_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 20, 1, 47, 0, 656942, tzinfo=utc)),
        ),
    ]
