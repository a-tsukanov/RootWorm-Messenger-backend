from rest_framework import serializers
from . import models
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelField):

    class Meta:
        model = User
        fields = ('username',)


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = models.Message
        fields = ('text', 'sender')
