from django.db import models
from datetime import datetime  

class Events(models.Model):
    # song title - s
    #"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    event_id = models.IntegerField(primary_key=True)
    event_state = models.BooleanField(default=True)
    title = models.CharField(max_length=255, null=False, default='title')
    event_date = models.DateField('Event Date', default=datetime.now, blank=True)
    start_time = models.TimeField(default='12:00:00')
    end_time = models.TimeField(default='12:00:00')
    venue = models.CharField(max_length=120,null=False, default='Venue')
    organizer = models.CharField(max_length=255, null=False,default='Organizer')
    description = models.TextField(blank=True)
    registration_link = models.CharField(max_length=255, null=True, default='registeration')
    photos_link = models.CharField(max_length=255, null=True, default='photos')
    medium_link = models.CharField(max_length=255, null=True, default='meduim')
    # name of artist or group/band
    def __str__(self):
        return "{} - {}".format(self.event_id, self.title)