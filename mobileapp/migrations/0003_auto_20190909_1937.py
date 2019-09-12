# Generated by Django 2.0.13 on 2019-09-09 19:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobileapp', '0002_auto_20190909_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='events',
            name='event_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Event Date'),
        ),
        migrations.AddField(
            model_name='events',
            name='venue',
            field=models.CharField(default='Venue', max_length=120),
        ),
        migrations.AlterField(
            model_name='events',
            name='organizer',
            field=models.CharField(default='Organizer', max_length=255),
        ),
        migrations.AlterField(
            model_name='events',
            name='title',
            field=models.CharField(default='title', max_length=255),
        ),
    ]
