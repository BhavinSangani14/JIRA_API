from django.shortcuts import render
from rest_framework import viewsets
from card_data.models import CardData
from card_data.serializer import CardDataSerializer
from rest_framework.decorators import action
from django.http import JsonResponse
# Create your views here.

class CardDataViewSet(viewsets.ModelViewSet):
    
    queryset = CardData.objects.all()
    serializer_class = CardDataSerializer
    
    @action(detail=True, methods=["get"])
    def fetch_data(self, request, pk=None):
        print("Get Jira card data")
        return JsonResponse({"type" : "jira card data"})