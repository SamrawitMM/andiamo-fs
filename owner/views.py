from django.shortcuts import render

from rest_framework import viewsets
from .models import TripHistory
from .serializers import TripHistorySerializer


class TripHistoryView(viewsets.ModelViewSet):
    queryset = TripHistory.objects.all()
    serializer_class = TripHistorySerializer