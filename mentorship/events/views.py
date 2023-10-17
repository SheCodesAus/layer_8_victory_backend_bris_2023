from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.db.models import Prefetch
from .models import Event, EventMentors
from users.models import CustomUser
from .serializers import EventSerializer, EventMentorsSerializer, EventDetailSerializer,EventMentorsDetailSerializer
from .permissions import IsSuperAdmin, CustomIsAdmin, IsValidMentor


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
            serializer.save(created_by=request.user, modified_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventDetail(APIView):
    permission_classes = [CustomIsAdmin]

    def get_object(self, pk):
        try:
            if self.request.user.is_staff:
                events = Event.objects.all()
            else:
                queryset = EventMentors.objects.all().filter(confirmed=True)
                events = (
                    Event.objects.all()
                    .filter(is_published=True)
                    .prefetch_related(Prefetch("event_mentors", queryset=queryset))
                )
            event = events.get(pk=pk)
            self.check_object_permissions(self.request, event)
            return event
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        event = self.get_object(pk)
        serializer = EventDetailSerializer(event)
        return Response(serializer.data)

    def put(self, request, pk):
        event = self.get_object(pk)
        serializer = EventDetailSerializer(
            instance=event, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventMentorList(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsValidMentor
    ]

    def get(self, request):
        if request.user.is_staff:
            event_mentors = EventMentors.objects.all()
        else:
            event_mentors = EventMentors.objects.all().filter(confirmed=True)
        serializer = EventMentorsSerializer(event_mentors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventMentorsSerializer(data=request.data)
        if request.user.is_staff:
            mentor_id_switch = CustomUser.objects.get(id=request.data['mentor_id'])
        else:
            mentor_id_switch = request.user
        if EventMentors.objects.filter(mentor_id=mentor_id_switch, event_id=request.data['event_id']).exists() == False:
            return Response("This mentor is already associated with this event", status=status.HTTP_400_BAD_REQUEST)
        else: 
            if Event.objects.get(id=request.data['event_id']).is_published:
                if serializer.is_valid():
                    serializer.save(
                        mentor_id=mentor_id_switch,
                        created_by=request.user,
                        modified_by=request.user,
                    )
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Event must be published before a mentor can be assigned", status=status.HTTP_400_BAD_REQUEST)

class EventMentorDetail(APIView):
    permission_classes = [CustomIsAdmin]

    def get_object(self,pk):
        try:
            if self.request.user.is_staff:
                event_mentors = EventMentors.objects.all()
            else:
                event_mentors = EventMentors.objects.all().filter(mentor_id=self.request.user.id)
            event_mentor = event_mentors.get(pk=pk)
            self.check_object_permissions(self.request,event_mentor)
            return event_mentor
        except EventMentors.DoesNotExist:
            raise Http404


    def get(self, request, pk):
        event_mentor = self.get_object(pk)
        serializer = EventMentorsDetailSerializer(event_mentor)
        return Response(serializer.data)

    def put(self, request, pk):
        event_mentor = self.get_object(pk)
        serializer = EventMentorsDetailSerializer(
            instance=event_mentor, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)