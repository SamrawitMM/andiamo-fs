from django.conf import settings
from rest_framework import serializers
from .models import CustomUser
class UserSerializer(serializers.ModelSerializer):
    # full_name = serializers.CharField(max_length=250)
    # phone_number = serializers.IntegerField()
    # username  = serializers.CharField(required=True)
    # email = serializers.EmailField()
    password  = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    class Meta:
        # model=settings.AUTH_USER_MODEL
        model=CustomUser
        # fields = '__all__'
        fields = ['username','email','full_name', 'phone_number','password']
        # exclude = ['Superuser status','Staff status','Date joined','Groups','User permissions']

    def create(self,validated_data):
        #  user = super().create(validated_data)
        # user.set_password(validated_data['password'])
        # user.save()
        user = settings.AUTH_USER_MODEL.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
        # user = User.objects.create_user(**validated_data)
        
    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        try:
            user.set_password(validated_data['password'])
            user.save()
        except KeyError:
            pass
        return user