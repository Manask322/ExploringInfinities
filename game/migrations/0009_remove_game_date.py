# Generated by Django 3.0.4 on 2020-03-29 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0008_auto_20200328_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='date',
        ),
    ]