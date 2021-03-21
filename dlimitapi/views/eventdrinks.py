from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from dlimitapi.models import Contact, Drink, Drinker, EventDrink, Event
import datetime


class EventDrinks(ViewSet):

    def create(self, request):
        drink = Drink.objects.get(pk= request.data["drink_id"])
        event = Event.objects.get(pk= request.data["event_id"])
        eventDrink = EventDrink()
        eventDrink.drink = drink
        eventDrink.event = event
        eventDrink.time_drank = datetime.datetime.now()

        try:
            eventDrink.save()
            serializer = EventDrinkSerializer(eventDrink, context={'request': request})
            return Response(serializer.data)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
       
        try:
            eventDrink = EventDrink.objects.get(pk=pk)
            serializer = EventDrinkSerializer(eventDrink, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)


    def destroy(self, request, pk=None):
        
        try:
            eventDrink = EventDrink.objects.get(pk=pk)
            eventDrink.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except EventDrink.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
       
        eventDrink = EventDrink.objects.all()

        serializer = EventDrinkSerializer(
            eventDrink, many=True, context={'request': request})
        return Response(serializer.data)

class EventDrinkSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = EventDrink
        fields = ('id', 'drink','event', 'time_drank')
        depth = 1