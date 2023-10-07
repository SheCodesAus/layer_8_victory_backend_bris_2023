from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from .models import Event, EventMentors
from .serializers import EventSerializer, EventMentorsSerializer
from .permissions import IsSuperAdmin


class EventList(APIView):

    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    @permission_classes(IsSuperAdmin)
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            if request.user.is_staff and request.user.is_superuser:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
