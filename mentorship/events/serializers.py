from rest_framework import serializers
from django.apps import apps

class EventSerializer(serializers.ModelSerializer):
  modified_by = serializers.ReadOnlyField(source='modified_by.id')
  created_by = serializers.ReadOnlyField(source='created_by.id')
  class Meta:
    model = apps.get_model('events.Event')
    fields = '__all__'

class EventMentorsSerializer(serializers.ModelSerializer):
  mentor_id = serializers.ReadOnlyField(source='mentor_id.id')
  modified_by = serializers.ReadOnlyField(source='modified_by.id')
  created_by = serializers.ReadOnlyField(source='created_by.id')
  class Meta:
    model = apps.get_model('events.EventMentors')
    fields = '__all__'

class EventDetailSerializer(EventSerializer):
  event_mentors = EventMentorsSerializer(many=True)

  def update(self,instance,validated_data):
    instance.title = validated_data.get('title', instance.title)
    instance.start_date = validated_data.get('start_date', instance.start_date)
    instance.end_date = validated_data.get('end_date', instance.end_date)
    instance.location = validated_data.get('location', instance.location)
    instance.is_published = validated_data.get('is_published', instance.is_published)
    instance.save()
    return instance

class EventMentorsDetailSerializer(EventMentorsSerializer):

  def update(self,instance,validated_data):
    instance.confirmed = validated_data.get('confirmed', instance.confirmed)
    instance.available = validated_data.get('available', instance.available)
    if instance.available == False:
        instance.confirmed = False
    instance.save()
    return instance

class MyEventsDetailSerializer(EventMentorsSerializer):
    def update(self,instance,validated_data):
      instance.available = validated_data.get('available', instance.available)
      instance.save()
      return instance