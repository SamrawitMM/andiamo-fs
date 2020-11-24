from rest_framework import serializers
from .models import TripHistory


class TripHistorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TripHistory
        fields = '__all__'