from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from dlimitapi.models import Contact


class Contacts(ViewSet):

    def retrieve(self, request, pk=None):
       
        try:
            contact = Contact.objects.get(pk=pk)
            serializer = ContactSerializer(contact, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
       
        contacts = Contact.objects.all()

        serializer = ContactSerializer(
            contacts, many=True, context={'request': request})
        return Response(serializer.data)

class ContactSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Contact
        fields = ('id', 'name', 'phone', 'drinker')