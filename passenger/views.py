from django.shortcuts import render
from rest_framework import viewsets,generics 
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PassengerSchedule , Passenger
from .serializers import PassengerScheduleSerializer ,PassengerSerializer
from django.conf import settings
# from .serializers import PassengerSerializer
# from .models import Passenger

from users.serializers import UserSerializer
class PassengerScheduleUpdateView(generics.RetrieveUpdateAPIView):
    queryset = PassengerSchedule.objects.all()
    serializer_class = PassengerScheduleSerializer

class PassengerScheduleCreateView(generics.CreateAPIView):
    queryset = PassengerSchedule.objects.all()
    serializer_class = PassengerScheduleSerializer

class PassengerScheduleView(generics.ListAPIView):

    # def get(self,request,*args, **kwargs):
        # passengerId = self.kwargs[self.lookup_url_kwarg]
        # return PassengerSchedule.objects.filter(passenger=pk)
    queryset = PassengerSchedule.objects.filter()
    serializer_class = PassengerScheduleSerializer
# class PassengerScheduleView(APIView):
    
    # def get(self,request,pk):
    #     passengerSchedule = PassengerSchedule.objects.filter(passenger=pk)
    #     print(passengerSchedule)
        # serializer = PassengerScheduleSerializer(passengerSchedule)
        # return Response(serializer.data)
    # queryset = PassengerSchedule.objects.all()
    # serializer_class = PassengerScheduleSerializer

class PassengerUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class PassengerCreateView(generics.CreateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

class PassengerView(generics.ListAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer