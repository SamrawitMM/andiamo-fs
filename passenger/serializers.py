from rest_framework import serializers
from .models import PassengerSchedule ,Passenger
# from .models import Passenger
from users.serializers import UserSerializer
from users.models import CustomUser
class PassengerScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassengerSchedule
        fields = '__all__'

# class PassengerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Passenger
#         fields = ('id', 'name')
class PassengerSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model=Passenger
        fields = '__all__'

    def create(self,validated_data):
        # print(validated_data)
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create(**user_data,user_type = 2)
        passenger = Passenger.objects.create(user=user,**validated_data)
        return passenger 

        