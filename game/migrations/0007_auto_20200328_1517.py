# Generated by Django 3.0.4 on 2020-03-28 15:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_auto_20200328_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 15, 17, 55, 179282, tzinfo=utc), null=True),
        ),
    ]
