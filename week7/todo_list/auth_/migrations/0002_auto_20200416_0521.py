# Generated by Django 3.0.4 on 2020-04-16 05:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auth_', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 16, 5, 21, 8, 248313, tzinfo=utc)),
        ),
    ]
