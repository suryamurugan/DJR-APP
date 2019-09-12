from rest_framework import serializers
from .models import Events


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ("event_id",'event_type',"title","event_date","start_time","end_time","venue","organizer","description")
