from rest_framework import serializers
from django.apps import apps

class EventSerializer(serializers.ModelSerializer):
  modified_by = serializers.ReadOnlyField(source='modified_by.id')
  class Meta:
    model = apps.get_model('events.Event')
    fields = '__all__'

class EventMentorsSerializer(serializers.ModelSerializer):
  class Meta:
    model = apps.get_model('events.EventMentors')
    fields = '__all__'

class EventDetailSerializer(EventSerializer):
  event_mentors = EventMentorsSerializer(many=True)