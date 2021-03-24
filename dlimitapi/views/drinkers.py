from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from dlimitapi.models import Drinker
from rest_framework import status



class Drinkers(ViewSet):

    def retrieve(self, request, pk=None):

        drinker = Drinker.objects.get(user=request.auth.user)
       
        try:
            serializer = DrinkerSerializer(drinker, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        
        drinker = Drinker.objects.get(user=request.auth.user)

        drinker.height = request.data["height"]
        drinker.age = request.data["age"]
        drinker.weight = request.data["weight"]
        

        drinker.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)


class DrinkerSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Drinker
        fields = ('id', 'height', 'age', 'weight')