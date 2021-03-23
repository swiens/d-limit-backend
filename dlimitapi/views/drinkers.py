from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from dlimitapi.models import Drinker


class Drinkers(ViewSet):

    def retrieve(self, request, pk=None):

        drinker = Drinker.objects.get(user=request.auth.user)
       
        try:
            serializer = DrinkerSerializer(drinker, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

class DrinkerSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Drinker
        fields = ('id', 'height', 'age', 'weight')