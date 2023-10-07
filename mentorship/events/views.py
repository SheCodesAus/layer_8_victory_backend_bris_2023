from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Event, EventMentors
from .serializers import EventSerializer, EventMentorsSerializer
from .permissions import IsSuperAdmin, CustomIsAdmin


class EventList(APIView):
    permission_classes = [CustomIsAdmin]
    def get(self, request):
        events = Event.objects.all()
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
