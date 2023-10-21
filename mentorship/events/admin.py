from django.contrib import admin
from django.contrib import admin
from events.models import Event, EventMentors

@admin.register(Event)
class ProjectAdmin(admin.ModelAdmin):
  pass

@admin.register(EventMentors)
class EventMentorsAdmin(admin.ModelAdmin):
  pass
