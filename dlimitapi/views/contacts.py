from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from dlimitapi.models import Contact, Drink, Drinker


class Contacts(ViewSet):

    def create(self, request):
       
        drinker = Drinker.objects.get(user=request.auth.user)

        
        contact = Contact()
        contact.name = request.data["name"]
        contact.phone = request.data["phone"]
        contact.drinker = drinker
    

        try:
            contact.save()
            serializer = ContactSerializer(contact, context={'request': request})
            return Response(serializer.data)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
       
        try:
            contact = Contact.objects.get(pk=pk)
            serializer = ContactSerializer(contact, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        
        drinker = Drinker.objects.get(user=request.auth.user)

        contact = Contact.objects.get(pk=pk)
        contact.name = request.data["name"]
        contact.phone = request.data["phone"]
        contact.drinker = drinker

        contact.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        
        try:
            contact = Contact.objects.get(pk=pk)
            contact.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Contact.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
       
        contacts = Contact.objects.all()

        serializer = ContactSerializer(
            contacts, many=True, context={'request': request})
        return Response(serializer.data)

class ContactSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Contact
        fields = ('id', 'name', 'phone', 'drinker')
        depth = 1