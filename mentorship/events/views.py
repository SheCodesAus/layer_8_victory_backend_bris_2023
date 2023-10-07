from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.db.models import Prefetch
from .models import Event, EventMentors
from .serializers import EventSerializer, EventMentorsSerializer, EventDetailSerializer
from .permissions import IsSuperAdmin, CustomIsAdmin


class EventList(APIView):
    permission_classes = [CustomIsAdmin]
    def get(self, request):
        if request.user.is_staff:
            events = Event.objects.all()
        else:
            events = Event.objects.all().filter(is_published=True)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(modified_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class EventDetail(APIView):
    permission_classes = [CustomIsAdmin]
    
    def get_object(self,pk):
        try:
            if self.request.user.is_staff:
                events = Event.objects.all()
            else:
                queryset = EventMentors.objects.all().filter(confirmed=True)
                events = Event.objects.all().filter(is_published=True).prefetch_related(Prefetch('event_mentors', queryset=queryset))
            event = events.get(pk=pk)
            self.check_object_permissions(self.request,event)
            return event
        except Event.DoesNotExist:
            raise Http404
    
    def get(self,request,pk):
        event = self.get_object(pk)

        serializer = EventDetailSerializer(event)
        return Response(serializer.data)

class EventMentorList(APIView):

    def get(self,request):
        if request.user.is_staff:
            event_mentors = EventMentors.objects.all()
        else:
            event_mentors = EventMentors.objects.all().filter(confirmed=True)
        serializer = EventMentorsSerializer(event_mentors, many=True)
        return Response(serializer.data)