# Generated by Django 3.0.4 on 2020-04-16 11:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auth_', '0005_auto_20200416_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 16, 11, 27, 20, 707479, tzinfo=utc)),
        ),
    ]