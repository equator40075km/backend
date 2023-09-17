from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = '__all__'

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        instance.user.first_name = user_data.get('first_name')
        instance.user.last_name = user_data.get('last_name')
        instance.user.save()

        instance.city = validated_data.get('city')
        instance.bday = validated_data.get('bday')
        instance.gender = validated_data.get('gender')
        instance.save()
        return instance
