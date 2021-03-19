from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from dlimitapi.models import Drink


class Drinks(ViewSet):

    def retrieve(self, request, pk=None):
       
        try:
            drink = Drink.objects.get(pk=pk)
            serializer = DrinkSerializer(drink, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
       
        drinks = Drink.objects.all()

        serializer = DrinkSerializer(
            drinks, many=True, context={'request': request})
        return Response(serializer.data)

class DrinkSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Drink
        fields = ('id', 'type')