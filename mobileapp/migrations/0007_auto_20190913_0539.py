# Generated by Django 2.0.13 on 2019-09-13 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobileapp', '0006_events_event_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='event_type',
        ),
        migrations.AddField(
            model_name='events',
            name='event_state',
            field=models.BooleanField(default=True),
        ),
    ]
