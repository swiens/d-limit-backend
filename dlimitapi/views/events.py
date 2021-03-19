from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from dlimitapi.models import Event


class Events(ViewSet):

    def retrieve(self, request, pk=None):
       
        try:
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(event, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
       
        events = Event.objects.all()

        serializer = EventSerializer(
            events, many=True, context={'request': request})
        return Response(serializer.data)

class EventSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Event
        fields = ('id', 'start_time', 'end_time', 'drinker')