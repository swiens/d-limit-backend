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


class Events(ViewSet):

    def create(self, request):
       
        drinker = Drinker.objects.get(user=request.auth.user)

        
        event = Event()
        event.start_time = request.data["name"]
        event.end_time = request.data["phone"]
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

        event = Evemt.objects.get(pk=pk)
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
        if game is not None:
            events = events.filter(event_id=event)


        serializer = EventSerializer(
            events, many=True, context={'request': request})
        return Response(serializer.data)

# class EventUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email']
# class EventDrinkerSerializer(serializers.ModelSerializer):
#     user = EventUserSerializer(many=False)
#     class Meta:
#         model = Drinker
#         fields = ['user']
class EventSerializer(serializers.ModelSerializer):
    # drinker = EventDrinkerSerializer(many=False)
    # drink = DrinkSerializer(many=False)
    class Meta:
        model = Event
        fields = ('id', 'start_time', 'end_time', 'drinker')



