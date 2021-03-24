from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from dlimitapi.models import Drink, Event, Drinker
from dlimitapi.views.drinks import DrinkSerializer
import datetime


class Events(ViewSet):

    def create(self, request):
       
        drinker = Drinker.objects.get(user=request.auth.user)

        event = Event()
        event.start_time = datetime.datetime.now()
        event.drinker = drinker
    
        try:
            event.save()
            serializer = EventSerializer(event, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
       
        try:
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(event, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        
        drinker = Drinker.objects.get(user=request.auth.user)

        event = Event.objects.get(pk=pk)
        event.start_time = request.data["start_time"]
        event.end_time = request.data["end_time"]
        event.drinker = drinker

        event.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        
        try:
            event = Event.objects.get(pk=pk)
            event.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Event.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
       
        events = Event.objects.all()

        event = self.request.query_params.get('eventId', None)
        if event is not None:
            events = events.filter(event_id=event)


        serializer = EventSerializer(
            events, many=True, context={'request': request})
        return Response(serializer.data)
    
    @action(detail=True, methods=['put'])
    def end_event(self, request, pk=None):
        event = Event.objects.get(pk=pk)
        event.end_time = datetime.datetime.now()
        event.departure = request.data["departure"]
        event.save()
        
        return Response({}, status=status.HTTP_204_NO_CONTENT)

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'start_time', 'end_time', 'drinker', 'departure')



