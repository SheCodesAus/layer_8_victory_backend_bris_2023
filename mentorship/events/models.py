from django.db import models
from django.contrib.auth import get_user_model

class Event(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='event_created'
    )
    last_modified = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='event_modified'
    )

class EventMentors(models.Model):
    event_id = models.ForeignKey(
        'Event',
        on_delete=models.CASCADE,
        related_name='event_mentors'
    )
    mentor_id = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='event_mentors'
    )
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='event_mentor_created'
    )
    last_modified = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='event_mentors_modified'
    )
    confirmed = models.BooleanField(default=False)
    available = models.BooleanField(default=True)