# Generated by Django 3.0.4 on 2020-04-16 05:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 16, 5, 35, 14, 28961, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 19, 5, 35, 14, 28983, tzinfo=utc)),
        ),
    ]
